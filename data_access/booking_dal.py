from data_access.base_dal import BaseDAL
from model.booking import Booking
from datetime import date

class BookingDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def get_by_id(self, booking_id: int) -> Booking:
        with self._connect() as conn:
            cursor = conn.execute("SELECT * FROM Booking WHERE booking_id=?", (booking_id,))
            row = cursor.fetchone()
        return self.__row_to_booking(row)

    def get_all(self) -> list[Booking]:
        with self._connect() as conn:
            cursor = conn.execute("SELECT * FROM Booking")
            rows = cursor.fetchall()
        return [self.__row_to_booking(row) for row in rows]

    def get_by_guest_id(self, guest_id: int, active_only: bool = False) -> list[Booking]:
        with self._connect() as conn:
            if active_only:
                cursor = conn.execute("SELECT * FROM Booking WHERE guest_id=? AND is_cancelled=0", (guest_id,))
            else:
                cursor = conn.execute("SELECT * FROM Booking WHERE guest_id=?", (guest_id,))
            rows = cursor.fetchall()
        return [self.__row_to_booking(row) for row in rows]

    def create_booking(self, booking: Booking) -> Booking:
        start_str = booking.check_in_date.isoformat() if hasattr(booking.check_in_date, "isoformat") else str(booking.check_in_date)
        end_str = booking.check_out_date.isoformat() if hasattr(booking.check_out_date, "isoformat") else str(booking.check_out_date)
        with self._connect() as conn:
            cursor = conn.execute(
                "INSERT INTO Booking (room_id, guest_id, check_in_date, check_out_date, is_cancelled, total_amount) VALUES (?, ?, ?, ?, ?, ?)",
                (booking.room_id, booking.guest_id, start_str, end_str, 0, booking.total_amount)
            )
            conn.commit()
            booking.booking_id = cursor.lastrowid
        booking.is_cancelled = False
        return booking

    def update_booking(self, booking: Booking) -> bool:
        start_str = booking.check_in_date.isoformat() if hasattr(booking.check_in_date, "isoformat") else str(booking.check_in_date)
        end_str = booking.check_out_date.isoformat() if hasattr(booking.check_out_date, "isoformat") else str(booking.check_out_date)
        status_val = 1 if booking.is_cancelled else 0
        with self._connect() as conn:
            result = conn.execute(
                "UPDATE Booking SET room_id=?, guest_id=?, check_in_date=?, check_out_date=?, is_cancelled=? WHERE booking_id=?",
                (booking.room_id, booking.guest_id, start_str, end_str, status_val, booking.booking_id)
            )
            conn.commit()
        return result.rowcount > 0

    def cancel_booking(self, booking_id: int) -> bool:
        with self._connect() as conn:
            result = conn.execute(
                "UPDATE Booking SET is_cancelled=1 WHERE booking_id=? AND is_cancelled=0",
                (booking_id,)
            )
            conn.commit()
        return result.rowcount > 0

    def is_room_available(self, room_id: int, check_in_date, check_out_date) -> bool:
        start_str = check_in_date.isoformat() if hasattr(check_in_date, "isoformat") else str(check_in_date)
        end_str = check_out_date.isoformat() if hasattr(check_out_date, "isoformat") else str(check_out_date)
        with self._connect() as conn:
            cursor = conn.execute(
                "SELECT booking_id FROM Booking WHERE room_id=? AND is_cancelled=0 AND ? < check_out_date AND ? > check_in_date",
                (room_id, start_str, end_str)
            )
            conflict = cursor.fetchone()
        return conflict is None

    def get_by_room_id(self, room_id: int) -> list[Booking]:
        with self._connect() as conn:
            cursor = conn.execute("SELECT * FROM Booking WHERE room_id=?", (room_id,))
            rows = cursor.fetchall()
        return [self.__row_to_booking(row) for row in rows]

    def get_by_date_range(self, check_in_date, check_out_date) -> list[Booking]:
        start_str = check_in_date.isoformat() if hasattr(check_in_date, "isoformat") else str(check_in_date)
        end_str = check_out_date.isoformat() if hasattr(check_out_date, "isoformat") else str(check_out_date)
        with self._connect() as conn:
            cursor = conn.execute(
                "SELECT * FROM Booking WHERE check_in_date <= ? AND check_out_date >= ?",
                (end_str, start_str)
            )
            rows = cursor.fetchall()
        return [self.__row_to_booking(row) for row in rows]

    def delete(self, booking_id: int) -> bool:
        with self._connect() as conn:
            result = conn.execute("DELETE FROM Booking WHERE booking_id=?", (booking_id,))
            conn.commit()
        return result.rowcount > 0
    
    def __row_to_booking(self, row) -> Booking | None:
        if row is None:
            return None
        return Booking(
            booking_id=row[0],
            guest_id=row[1],
            room_id=row[2],
            check_in=row[3],
            check_out=row[4],
            is_cancelled=bool(row[5]),
            total_amount=row[6]
        )