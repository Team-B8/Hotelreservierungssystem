from data_access.hotel_dal import HotelDAL
from model.hotel import Hotel

class HotelManager:
    def __init__(self):
        self.__hotel_dal = HotelDAL()

    def get_hotel(self, hotel_id: int) -> Hotel | None:
        return self.__hotel_dal.get_hotel_by_id(hotel_id)

    def delete_hotel(self, hotel_id: int) -> None:
        self.__hotel_dal.delete_hotel_by_id(hotel_id)

    def add_hotel(self, hotel: Hotel) -> None:
        self.__hotel_dal.insert_hotel(hotel)

    def update_hotel_name(self, hotel_id: int, new_name: str) -> None:
        self.__hotel_dal.update_hotel_name(hotel_id, new_name)

    def update_hotel_stars(self, hotel_id: int, new_stars: int) -> None:
        self.__hotel_dal.update_hotel_stars(hotel_id, new_stars)
