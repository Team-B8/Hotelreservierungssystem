from model.hotel import hotel
from data_access.hotel_dal import HotelDAL

class HotelManager:
    def __init__(self) -> None:
        self.__hotel_dal = data_access.HotelDAL()

    def create_hotel(self, name: str, stars: int) -> model.Hotel:
        # Business-Logik: Stars müssen zwischen 1 und 5 sein
        if not (1 <= stars <= 5):
            raise ValueError("Stars must be between 1 and 5")
        return self.__hotel_dal.create_hotel(name, stars)

    def get_hotel(self, hotel_id: int) -> model.Hotel | None:
        return self.__hotel_dal.read_hotel_by_id(hotel_id)

    def delete_hotel(self, hotel_id: int) -> None:
        self.__hotel_dal.delete_hotel(hotel_id)

