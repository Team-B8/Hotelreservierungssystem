from data_access.base_dal import BaseDal
from model.hotel import Hotel

class HotelDAL(BaseDal):
    def create_hotel(self, name: str, stars: int, address_id: int) -> Hotel:
        sql = "INSERT INTO Hotel (name, stars, address_id) VALUES (?, ?, ?)"
        params = (name, stars, address_id)
        last_row_id, _ = self.execute(sql, params)
        return Hotel(hotel_id=last_row_id, name=name, stars=stars, address_id=address_id)

    def read_hotel_by_id(self, hotel_id: int) -> Hotel | None:
        sql = "SELECT hotel_id, name, stars, address_id FROM Hotel WHERE hotel_id = ?"
        params = (hotel_id,)
        row = self.fetchone(sql, params)
        if row:
            return Hotel(hotel_id=row[0], name=row[1], stars=row[2], address_id=row[3])
        return None

    def get_all_hotels(self) -> list[Hotel]:
        sql = "SELECT hotel_id, name, stars, address_id FROM Hotel"
        rows = self.fetchall(sql)
        return [Hotel(hotel_id=row[0], name=row[1], stars=row[2], address_id=row[3]) for row in rows]
    
    def update_hotel(self, hotel_id: int, name: str, stars: int) -> bool:
        sql = "UPDATE Hotel SET name = ?, stars = ? WHERE hotel_id = ?"
        params = (name, stars, hotel_id)
        _, rowcount = self.execute(sql, params)
        return rowcount > 0

    def delete_hotel(self, hotel_id: int) -> bool:
        sql = "DELETE FROM Hotel WHERE hotel_id = ?"
        params = (hotel_id,)
        _, rowcount = self.execute(sql, params)
        return rowcount > 0
