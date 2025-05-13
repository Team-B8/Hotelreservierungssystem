from data_access.base_dal import BaseDal
from model.hotel import Hotel

class HotelDAL(BaseDal):
    def create_hotel(self, name: str, stars: int) -> model.Hotel:
        sql = "
        INSERT INTO Hotel (Name, Stars) VALUES (?, ?)
        "
        params = (name, stars)
        last_row_id, _ = self.execute(sql, params)
        return model.Hotel(last_row_id, name, stars)

    def read_hotel_by_id(self, hotel_id: int) -> model.Hotel | None:
        sql = "
        SELECT HotelId, Name, Stars FROM Hotel WHERE HotelId = ?
        "
        params = (hotel_id,)
        result = self.fetchone(sql, params)
        if result:
            hotel_id, name, stars = result
            return model.Hotel(hotel_id, name, stars)
        return None

    def delete_hotel(self, hotel_id: int) -> None:
        sql = "DELETE FROM Hotel WHERE HotelId = ?"
        params = (hotel_id,)
        self.execute(sql, params)
