from data_access.base_dal import BaseDal
from model.booking import Booking
from model.room import Room

from datetime import datetime

class BookingDAL(BaseDal):
    def create_booking(self, guest_id: int, room: Room, check_in: datetime, check_out: datetime, total_amount: float) -> Booking:
        sql = """
            INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
            VALUES (?, ?, ?, ?, 0, ?)
        """
        params = (guest_id, room.room_id, check_in, check_out, total_amount)
        last_id, _ = self.execute(sql, params)
        return Booking(last_id, guest_id, room, check_in, check_out, False, total_amount)

    def get_booking_by_id(self, booking_id: int) -> Booking | None:
        sql = "SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount FROM Booking WHERE booking_id = ?"
        result = self.fetchone(sql, (booking_id,))
        if result:
            booking_id, guest_id, room_id, check_in, check_out, is_cancelled, total = result
            room = self.get_room_by_id(room_id) 
            return Booking(booking_id, guest_id, room, check_in, check_out, bool(is_cancelled), total)
        return None

    def cancel_booking(self, booking_id: int):
        sql = "UPDATE Booking SET is_cancelled = 1 WHERE booking_id = ?"
        self.execute(sql, (booking_id,))
