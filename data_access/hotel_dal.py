from data_access.base_dal import BaseDAL
from model.hotel import Hotel

class HotelDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def create_hotel(self, name: str, stars: int, address_id: int) -> Hotel:
        # SQL query to insert a new hotel into the database
        sql = "INSERT INTO Hotel (name, stars, address_id) VALUES (?, ?, ?)"
        params = (name, stars, address_id)
        # connect to the database and run the insert query
        with self._connect() as conn:
            cursor = conn.execute(sql, params)
            conn.commit()
            last_row_id = cursor.lastrowid
        # return a Hotel object with the new data
        return Hotel(hotel_id=last_row_id, name=name, stars=stars, address_id=address_id)

    def read_hotel_by_id(self, hotel_id: int) -> Hotel | None:
        sql = "SELECT hotel_id, name, stars, address_id FROM Hotel WHERE hotel_id = ?"
        params = (hotel_id,)
        with self._connect() as conn:
            cursor = conn.execute(sql, params)
            row = cursor.fetchone()
        if row:
            return Hotel(hotel_id=row[0], name=row[1], stars=row[2], address_id=row[3])
        return None

    def get_all_hotels(self) -> list[Hotel]:
        sql = "SELECT hotel_id, name, stars, address_id FROM Hotel"
        with self._connect() as conn:
            cursor = conn.execute(sql)
            rows = cursor.fetchall()
        return [Hotel(hotel_id=row[0], name=row[1], stars=row[2], address_id=row[3]) for row in rows]
    
    def update_hotel(self, hotel_id: int, name: str, stars: int) -> bool:
        # SQL query to update hotel name and stars by hotel ID
        sql = "UPDATE Hotel SET name = ?, stars = ? WHERE hotel_id = ?"
        params = (name, stars, hotel_id)
        # connect to the database and run the update
        with self._connect() as conn:
            cursor = conn.execute(sql, params)
            conn.commit()
        # return True if at least one row was updated
        return cursor.rowcount > 0

    def delete_hotel(self, hotel_id: int) -> bool:
        sql = "DELETE FROM Hotel WHERE hotel_id = ?"
        params = (hotel_id,)
        with self._connect() as conn:
            cursor = conn.execute(sql, params)
            conn.commit()
        return cursor.rowcount > 0
