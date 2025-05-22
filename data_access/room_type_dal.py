from data_access.base_dal import BaseDAL
from model.room_type import RoomType

class RoomTypeDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def get_by_id(self, type_id: int) -> RoomType | None:
        # SQL query to get a room type by its ID
        sql = "SELECT * FROM room_type WHERE type_id = ?"
        # get the first matching row from the database
        row = self.fetchone(sql, (type_id,))
        # if a row is found, create and return a RoomType object
        if row:
            return RoomType(
                room_type_id=row[0],
                description=row[1],
                max_guests=row[2]
            )
        # if no row found, return None
        return None

    def get_all(self) -> list[RoomType]:
        sql = "SELECT * FROM room_type"
        rows = self.fetchall(sql)
        return [
            RoomType(
                room_type_id=row[0],
                description=row[1],
                max_guests=row[2]
            ) for row in rows
        ]