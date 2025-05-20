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

    def update_hotel(self, hotel_id: int, name: str, stars: int) -> bool:
        if not (1 <= stars <= 5):
            raise ValueError("Stars must be between 1 and 5")
        return self.hotel_dal.update_hotel(hotel_id, name, stars)

    def get_all_hotels(self) -> list[Hotel]:
        return self.hotel_dal.get_all_hotels()
    
    def filter_by_city(self, city: str) -> list[Hotel]:
        # get all hotels from the database
        hotels = self.hotel_dal.get_all_hotels()
        # return only hotels where the city matches
        return [h for h in hotels if self.address_dal.get_address_by_hotel(h.hotel_id).city.lower() == city.lower()]

    def filter_by_city_and_stars(self, city: str, min_stars: int) -> list[Hotel]:
        # get hotels in the given city
        hotels = self.filter_by_city(city)
        # return only hotels with stars >= min_stars
        return [h for h in hotels if h.stars >= min_stars]

    def filter_by_city_and_guest_capacity(self, city: str, guests: int) -> list[Hotel]:
        hotels = self.filter_by_city(city)
        matching_hotels = []
        for hotel in hotels:
            rooms = self.room_dal.get_rooms_by_hotel_id(hotel.hotel_id)
            for room in rooms:
                room_type = self.room_type_dal.get_by_id(room.type_id)
                if room_type.max_guests >= guests:
                    matching_hotels.append(hotel)
                    break
        return matching_hotels
    
    def filter_by_availability(self, city: str, check_in: date, check_out: date) -> list[Hotel]:
        hotels = self.filter_by_city(city)
        available_hotels = []
        for hotel in hotels:
            rooms = self.room_dal.get_rooms_by_hotel_id(hotel.hotel_id)
            for room in rooms:
                if self.booking_dal.is_room_available(room.room_id, check_in, check_out):
                    available_hotels.append(hotel)
                    break
        return available_hotels

    def filter_combined(self, city: str, guests: int, min_stars: int, check_in: date, check_out: date) -> list[Hotel]:
        hotels = self.filter_by_city_and_stars(city, min_stars)
        matching_hotels = []
        for hotel in hotels:
            rooms = self.room_dal.get_rooms_by_hotel_id(hotel.hotel_id)
            for room in rooms:
                room_type = self.room_type_dal.get_by_id(room.type_id)
                if room_type.max_guests >= guests and self.booking_dal.is_room_available(room.room_id, check_in, check_out):
                    matching_hotels.append(hotel)
                    break
        return matching_hotels