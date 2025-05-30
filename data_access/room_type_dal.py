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
    
    def create_room_type(self, description: str, max_guests: int) -> RoomType:
        # SQL to insert a new room type into the database
        sql = "INSERT INTO room_type (description, max_guests) VALUES (?, ?)"
        # connect to the database and execute the insert
        with self._connect() as conn:
            cursor = conn.execute(sql, (description, max_guests))
            conn.commit()  # save the changes
            new_id = cursor.lastrowid  # get the ID of the new room type
        # return a RoomType object with the inserted data
        return RoomType(type_id=new_id, description=description, max_guests=max_guests)

    def update_room_type(self, type_id: int, description: str, max_guests: int) -> bool:
        # SQL to update a room type based on its ID
        sql = "UPDATE room_type SET description = ?, max_guests = ? WHERE type_id = ?"
        # connect and execute the update
        with self._connect() as conn:
            cursor = conn.execute(sql, (description, max_guests, type_id))
            conn.commit()  # save the changes
        # return True if at least one row was updated
        return cursor.rowcount > 0
    
    def delete_room_type(self, type_id: int) -> bool:
        # SQL to delete a room type by its ID
        sql = "DELETE FROM room_type WHERE type_id = ?"
        # connect and execute the delete
        with self._connect() as conn:
            cursor = conn.execute(sql, (type_id,))
            conn.commit()  # save the changes
        # return True if a row was deleted
        return cursor.rowcount > 0
    
    def is_type_in_use(self, type_id: int) -> bool:
        # SQL to delete a room type by its ID
        sql = "SELECT COUNT(*) FROM room WHERE type_id = ?"
        with self._connect() as conn:
            cursor = conn.execute(sql, (type_id,))
            count = cursor.fetchone()[0]
        return count > 0