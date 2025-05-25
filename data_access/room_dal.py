from data_access.base_dal import BaseDAL
from model.room import Room

class RoomDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def get_by_id(self, room_id: int) -> Room | None:
        sql = "SELECT * FROM room WHERE room_id = ?"
        row = self.fetchone(sql, (room_id,))
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
        # SQL query to get all rooms for the given hotel ID
        sql = "SELECT * FROM room WHERE hotel_id = ?"
        # get all matching rows from the database
        rows = self.fetchall(sql, (hotel_id,))
        # create a list of Room objects from the rows
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
        rows = self.fetchall(sql)
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
        # SQL query to find booked rooms in the given hotel and date range
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
        # get all matching rows from the database
        rows = self.fetchall(sql, (hotel_id, check_out, check_in, check_in, check_out))
        # return only the room IDs from the result
        return [row[0] for row in rows]