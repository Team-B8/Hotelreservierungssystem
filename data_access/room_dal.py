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