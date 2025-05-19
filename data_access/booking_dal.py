from data_access.base_dal import BaseDAL
from model.booking import Booking
from datetime import date

class BookingDAL(BaseDAL):
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

    def create_booking(self, booking: Booking) -> Booking:
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

    def update_booking(self, booking: Booking) -> bool:
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

    def get_by_room_id(self, room_id: int) -> list[Booking]:
        cursor = self.conn.execute("SELECT * FROM bookings WHERE room_id=?", (room_id,))
        rows = cursor.fetchall()
        return [self.__row_to_booking(row) for row in rows]

    def get_by_date_range(self, start_date, end_date) -> list[Booking]:
        start_str = start_date.isoformat() if hasattr(start_date, "isoformat") else str(start_date)
        end_str = end_date.isoformat() if hasattr(end_date, "isoformat") else str(end_date)
        cursor = self.conn.execute(
            "SELECT * FROM bookings WHERE start_date <= ? AND end_date >= ?",
            (end_str, start_str)
        )
        rows = cursor.fetchall()
        return [self.__row_to_booking(row) for row in rows]

    def delete(self, booking_id: int) -> bool:
        result = self.conn.execute("DELETE FROM bookings WHERE id=?", (booking_id,))
        self.conn.commit()
        return result.rowcount > 0