from data_access.base_dal import BaseDAL
from model.booking import Booking
from datetime import date

class BookingDAL(BaseDAL):
    """Data access layer for the bookings table."""
    def __row_to_booking(self, row) -> Booking:
        if not row:
            return None
        # Convert database row to Booking object (including date and status conversions)
        booking = Booking(**row)
        # Convert dates from string to date object if needed
        if isinstance(booking.start_date, str):
            booking.start_date = date.fromisoformat(booking.start_date)
        if isinstance(booking.end_date, str):
            booking.end_date = date.fromisoformat(booking.end_date)
        # Convert status 0/1 to bool
        booking.status = bool(booking.status)
        return booking

    def get_by_id(self, booking_id: int) -> Booking:
        cursor = self.conn.execute("SELECT * FROM bookings WHERE id=?", (booking_id,))
        row = cursor.fetchone()
        return self.__row_to_booking(row)

    def get_all(self) -> list[Booking]:
        cursor = self.conn.execute("SELECT * FROM bookings")
        rows = cursor.fetchall()
        return [self.__row_to_booking(row) for row in rows]

    def get_by_guest_id(self, guest_id: int, active_only: bool = False) -> list[Booking]:
        if active_only:
            cursor = self.conn.execute("SELECT * FROM bookings WHERE guest_id=? AND status=0", (guest_id,))
        else:
            cursor = self.conn.execute("SELECT * FROM bookings WHERE guest_id=?", (guest_id,))
        rows = cursor.fetchall()
        return [self.__row_to_booking(row) for row in rows]

    def create(self, booking: Booking) -> Booking:
        # Store dates as ISO format strings
        start_str = booking.start_date.isoformat() if hasattr(booking.start_date, "isoformat") else str(booking.start_date)
        end_str = booking.end_date.isoformat() if hasattr(booking.end_date, "isoformat") else str(booking.end_date)
        cursor = self.conn.execute(
            "INSERT INTO bookings (room_id, guest_id, start_date, end_date, status) VALUES (?, ?, ?, ?, ?)",
            (booking.room_id, booking.guest_id, start_str, end_str, 0)
        )
        self.conn.commit()
        booking.id = cursor.lastrowid
        booking.status = False
        return booking

    def update(self, booking: Booking) -> bool:
        start_str = booking.start_date.isoformat() if hasattr(booking.start_date, "isoformat") else str(booking.start_date)
        end_str = booking.end_date.isoformat() if hasattr(booking.end_date, "isoformat") else str(booking.end_date)
        status_val = 1 if booking.status else 0
        result = self.conn.execute(
            "UPDATE bookings SET room_id=?, guest_id=?, start_date=?, end_date=?, status=? WHERE id=?",
            (booking.room_id, booking.guest_id, start_str, end_str, status_val, booking.id)
        )
        self.conn.commit()
        return result.rowcount > 0

    def cancel_booking(self, booking_id: int) -> bool:
        result = self.conn.execute(
            "UPDATE bookings SET status=1 WHERE id=? AND status=0",
            (booking_id,)
        )
        self.conn.commit()
        return result.rowcount > 0

    def is_room_available(self, room_id: int, start_date, end_date) -> bool:
        # Check if given room has any active booking overlapping the date range
        start_str = start_date.isoformat() if hasattr(start_date, "isoformat") else str(start_date)
        end_str = end_date.isoformat() if hasattr(end_date, "isoformat") else str(end_date)
        cursor = self.conn.execute(
            "SELECT id FROM bookings WHERE room_id=? AND status=0 AND ? < end_date AND ? > start_date",
            (room_id, start_str, end_str)
        )
        conflict = cursor.fetchone()
        return conflict is None