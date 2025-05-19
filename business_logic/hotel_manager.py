from data_access.hotel_dal import HotelDAL
from data_access.address_dal import AddressDAL
from data_access.room_dal import RoomDAL
from data_access.room_type_dal import RoomTypeDAL
from data_access.booking_dal import BookingDAL
from model.hotel import Hotel
from datetime import date

class HotelManager:
    def __init__(self):
        self.hotel_dal = HotelDAL()
        self.address_dal = AddressDAL()
        self.room_dal = RoomDAL()
        self.room_type_dal = RoomTypeDAL()
        self.booking_dal = BookingDAL()

    def create_hotel(self, name: str, stars: int) -> Hotel:
        if not (1 <= stars <= 5):
            raise ValueError("Stars must be between 1 and 5")
        return self.hotel_dal.create_hotel(name, stars)

    def get_hotel(self, hotel_id: int) -> Hotel | None:
        return self.hotel_dal.read_hotel_by_id(hotel_id)

    def delete_hotel(self, hotel_id: int) -> None:
        self.hotel_dal.delete_hotel(hotel_id)

