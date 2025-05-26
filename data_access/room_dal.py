from data_access.base_dal import BaseDAL
from model.room import Room

class RoomDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def get_by_id(self, room_id: int) -> Room | None:
        sql = "SELECT * FROM room WHERE room_id = ?"
        with self._connect() as conn:
            cursor = conn.execute(sql, (room_id,))
            row = cursor.fetchone()
        if row:
            return Room(
                room_id=row[0],
                hotel_id=row[1],
                room_no=row[2],
                type_id=row[3],
                price_per_night=row[4]
            )
        return None

    def get_rooms_by_hotel_id(self, hotel_id: int) -> list[Room]:
        sql = "SELECT * FROM room WHERE hotel_id = ?"
        with self._connect() as conn:
            cursor = conn.execute(sql, (hotel_id,))
            rows = cursor.fetchall()
        return [
            Room(
                room_id=row[0],
                hotel_id=row[1],
                room_no=row[2],
                type_id=row[3],
                price_per_night=row[4]
            )
            for row in rows
        ]

    def get_all_rooms(self) -> list[Room]:
        sql = "SELECT * FROM room"
        with self._connect() as conn:
            cursor = conn.execute(sql)
            rows = cursor.fetchall()
        return [
            Room(
                room_id=row[0],
                hotel_id=row[1],
                room_no=row[2],
                type_id=row[3],
                price_per_night=row[4]
            )
            for row in rows
        ]
    

    def get_booked_room_ids(self, hotel_id: int, check_in: str, check_out: str) -> list[int]:
        sql = """
            SELECT DISTINCT r.room_id
            FROM room r
            JOIN booking b ON r.room_id = b.room_id
            WHERE r.hotel_id = ?
            AND b.is_cancelled = 0
            AND (
                (b.check_in_date < ? AND b.check_out_date > ?) OR
                (b.check_in_date >= ? AND b.check_in_date < ?)
            )
        """
        with self._connect() as conn:
            cursor = conn.execute(sql, (hotel_id, check_out, check_in, check_in, check_out))
            rows = cursor.fetchall()
        return [row[0] for row in rows]
    
    def create_room(self, hotel_id: int, room_no: str, type_id: int, price_per_night: float) -> int:
        sql = "INSERT INTO room (hotel_id, room_number, type_id, price_per_night) VALUES (?, ?, ?, ?)"
        params = (hotel_id, room_no, type_id, price_per_night)
        return self.insert_and_get_id(sql, params)