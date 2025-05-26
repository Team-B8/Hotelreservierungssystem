from data_access.base_dal import BaseDAL
from model.room_type import RoomType

class RoomTypeDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def get_by_id(self, type_id: int) -> RoomType | None:
        sql = "SELECT * FROM room_type WHERE type_id = ?"
        with self._connect() as conn:
            cursor = conn.execute(sql, (type_id,))
            row = cursor.fetchone()
        if row:
            return RoomType(
                type_id=row[0],
                description=row[1],
                max_guests=row[2]
            )
        return None

    def get_all(self) -> list[RoomType]:
        sql = "SELECT * FROM room_type"
        with self._connect() as conn:
            cursor = conn.execute(sql)
            rows = cursor.fetchall()
        return [
            RoomType(
                type_id=row[0],
                description=row[1],
                max_guests=row[2]
            ) for row in rows
        ]