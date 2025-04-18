from data_access.hotel_dal import HotelDAL
from model.hotel import Hotel

class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int):
        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars

    def get_hotel_id(self) -> int:
        return self.__hotel_id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_stars(self) -> int:
        return self.__stars

    def set_stars(self, stars: int) -> None:
        self.__stars = stars

    def delete(self) -> None:
        del self

    def get_rooms(self) -> list:
        # Placeholder for getting rooms associated with the hotel
        return []

    def get_available_rooms(self, start: str, end: str) -> list:
        # Placeholder for checking available rooms in the given date range
        return []
