from data_access.base_dal import BaseDAL
from model.booking import Booking
from datetime import date

class BookingDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def get_by_id(self, booking_id: int) -> Booking:
        # Get one booking by ID, used to look up a specific booking in the DB
        with self._connect() as conn:
            cursor = conn.execute("SELECT * FROM Booking WHERE booking_id=?", (booking_id,))
            row = cursor.fetchone()
        return self.__row_to_booking(row)

    def get_by_guest_id(self, guest_id: int, active_only: bool = False) -> list[Booking]:
        # Returns all bookings for a given guest_id, optionally only active (not cancelled) bookings
        with self._connect() as conn:
            if active_only:
                cursor = conn.execute("SELECT * FROM Booking WHERE guest_id=? AND is_cancelled=0", (guest_id,))
            else:
                cursor = conn.execute("SELECT * FROM Booking WHERE guest_id=?", (guest_id,))
            rows = cursor.fetchall()
        return [self.__row_to_booking(row) for row in rows]

    def create_booking(self, booking: Booking) -> Booking:
        # convert dates to string format (ISO)
        start_str = booking.check_in.isoformat() if hasattr(booking.check_in, "isoformat") else str(booking.check_in)
        end_str = booking.check_out.isoformat() if hasattr(booking.check_out, "isoformat") else str(booking.check_out)        # connect to the database and insert the booking
        with self._connect() as conn:
            cursor = conn.execute(
                "INSERT INTO Booking (room_id, guest_id, check_in_date, check_out_date, is_cancelled, total_amount) VALUES (?, ?, ?, ?, ?, ?)",
    (booking.room_id, booking.guest_id, start_str, end_str, 0, booking.total_amount)
            )
            conn.commit()
            # store the new booking ID
            booking.booking_id = cursor.lastrowid
        # set cancellation flag to False
        booking.is_cancelled = False
        # return the saved booking object
        return booking

    def cancel_booking(self, booking_id: int) -> bool:
        # connect to the database and update the booking to set it as cancelled
        with self._connect() as conn:
            result = conn.execute(
                "UPDATE Booking SET is_cancelled=1 WHERE booking_id=? AND is_cancelled=0",
                (booking_id,)
            )
            conn.commit()
        return result.rowcount > 0

    def is_room_available(self, room_id: int, check_in_date, check_out_date) -> bool:
        # Checks if a room is available between the given check-in and check-out dates
        start_str = check_in_date.isoformat() if hasattr(check_in_date, "isoformat") else str(check_in_date)
        end_str = check_out_date.isoformat() if hasattr(check_out_date, "isoformat") else str(check_out_date)
        with self._connect() as conn:
            cursor = conn.execute(
                "SELECT booking_id FROM Booking WHERE room_id=? AND is_cancelled=0 AND ? < check_out_date AND ? > check_in_date",
                (room_id, start_str, end_str)
            )
            conflict = cursor.fetchone()
        return conflict is None
    
    def __row_to_booking(self, row) -> Booking | None:
        # Converts a database row into a Booking object, returns None if the row is empty
        if row is None:
            return None
        return Booking(
            booking_id=row[0],
            guest_id=row[1],
            room_id=row[2],
            check_in=row[3],
            check_out=row[4],
            is_cancelled=bool(row[5]),
            total_amount=row[6],
        )
    
    def get_by_guest_email(self, email: str) -> list[Booking]:
        # SQL query to get all bookings for a guest using their email
        sql = """SELECT b.* FROM Booking b JOIN Guest g ON b.guest_id = g.guest_id WHERE g.email = ?"""
        # connect to the database and run the query
        with self._connect() as conn:
            cursor = conn.execute(sql, (email,))
            rows = cursor.fetchall()
        # convert each row to a Booking object and return the list
        return [self.__row_to_booking(row) for row in rows]
    
    def get_all_bookings_with_details(self) -> list[tuple]:
        # get all information for the booking
        sql = """SELECT b.booking_id, g.first_name || ' ' || g.last_name AS guest_name, r.room_number, h.name AS hotel_name, b.check_in_date, b.check_out_date, b.total_amount, b.is_cancelled FROM Booking b JOIN Guest g ON b.guest_id = g.guest_id JOIN Room r ON b.room_id = r.room_id JOIN Hotel h ON r.hotel_id = h.hotel_id ORDER BY b.check_in_date DESC"""
        with self._connect() as conn:
            cursor = conn.execute(sql)
            return cursor.fetchall()
    
    def get_room_type_occupancy_by_hotel(self, hotel_id: int) -> list[tuple[str, int]]:
        # Returns a list of tuples (room_type_description, count_of_bookings) for the given hotel.
        # SQL-Query counts how often a room_type was booked (not cancelled)
        sql = """
        SELECT rt.description, COUNT(b.booking_id) as bookings
        FROM Booking b
        JOIN Room r ON b.room_id = r.room_id
        JOIN Room_Type rt ON r.type_id = rt.type_id
        WHERE r.hotel_id = ? AND b.is_cancelled = 0
        GROUP BY rt.description
        ORDER BY bookings DESC
        """
        # connect to the database and run the query
        with self._connect() as conn:
            cursor = conn.execute(sql, (hotel_id,))
            return cursor.fetchall()

    def has_completed_booking(self, check_out_date: date) -> bool:
        # Check if there exists at least one completed (not cancelled) booking where the check-out date is in the past and matches the given date
        sql = """
        SELECT 1 FROM Booking
        WHERE check_out_date = ?
        AND is_cancelled = 0
        AND check_out_date < DATE('now')
        LIMIT 1
        """
        with self._connect() as conn:
            cursor = conn.execute(sql, (check_out_date,))
            # Returns True if a matching row is found, otherwise False
            return cursor.fetchone() is not None

    def get_completed_bookings_by_guest_id(self, guest_id: int) -> list:
        # Retrieve all bookings for a guest that are completed (i.e. past and not cancelled)
        sql = """
            SELECT booking_id, room_id, check_in_date, check_out_date
            FROM Booking
            WHERE guest_id = ?
            AND is_cancelled = 0
            AND check_out_date <= DATE('now')
            """
        with self._connect() as conn:
            cursor = conn.execute(sql, (guest_id,))
        # Returns a list of all matching booking rows
        return cursor.fetchall()
