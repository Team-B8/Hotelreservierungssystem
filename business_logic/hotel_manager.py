from data_access.hotel_dal import HotelDAL
from data_access.address_dal import AddressDAL
from data_access.room_dal import RoomDAL
from data_access.room_type_dal import RoomTypeDAL
from data_access.booking_dal import BookingDAL
from model.hotel import Hotel
from model.room import Room
from datetime import date

class HotelManager:
    def __init__(self):
        self.hotel_dal = HotelDAL()
        self.address_dal = AddressDAL()
        self.room_dal = RoomDAL()
        self.room_type_dal = RoomTypeDAL()
        self.booking_dal = BookingDAL()

    def create_hotel(self, name: str, stars: int, address_id: int):
        # check if stars are in the valid range
        if not (1 <= stars <= 5):
            raise ValueError("Die Sterne müssen zwischen 1 und 5 liegen.")
        # create the hotel in the database
        hotel = self.hotel_dal.create_hotel(name, stars, address_id)
        # get the default room type (ID 1, usually Single room)
        default_type = self.room_type_dal.get_by_id(1)
        # if default room type doesn't exist, raise an error
        if not default_type:
            raise ValueError("Standard-Raumtyp (ID 1) ist nicht vorhanden")
        # create a default room for the new hotel
        room = self.room_dal.create_room(hotel.hotel_id, "001", default_type.type_id, 100.0)
        # return the created hotel
        return hotel

    def get_hotel(self, hotel_id: int) -> Hotel | None:
        return self.hotel_dal.read_hotel_by_id(hotel_id)

    def delete_hotel(self, hotel_id: int) -> bool:
        # get the hotel by ID
        hotel = self.get_hotel(hotel_id)
        # if hotel does not exist, return False
        if not hotel:
            return False
        # delete the hotel using the data access layer and return the result
        return self.hotel_dal.delete_hotel(hotel_id)

    def update_hotel(self, hotel_id: int, name: str, stars: int, address=None) -> bool:
        # check if stars are in the valid range
        if not (1 <= stars <= 5):
            raise ValueError("Sterne müssen zwischen 1 und 5 liegen")
        # update hotel name and stars in the database
        hotel_updated = self.hotel_dal.update_hotel(hotel_id, name, stars)
        # if an address object is given, update the address too
        if address:
            self.address_dal.update_address(address)
        # return True if hotel was updated
        return hotel_updated

    def get_all_hotels(self) -> list[Hotel]:
        # get all hotels from the database
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
        # get hotels in the given city
        hotels = self.filter_by_city(city)
        # list to store hotels that have rooms for the guests
        matching_hotels = []
        # check each hotel
        for hotel in hotels:
            # get all rooms for the hotel
            rooms = self.room_dal.get_rooms_by_hotel_id(hotel.hotel_id)
            # check each room
            for room in rooms:
                # get room type to check max guests
                room_type = self.room_type_dal.get_by_id(room.type_id)
                # if room can fit the number of guests
                if room_type.max_guests >= guests:
                    # add hotel to result and stop checking more rooms
                    matching_hotels.append(hotel)
                    break
        # return hotels with suitable rooms
        return matching_hotels
    
    def filter_by_availability(self, city: str, check_in: date, check_out: date) -> list[Hotel]:
        # get hotels in the given city
        hotels = self.filter_by_city(city)
        # list to store hotels with at least one available room
        available_hotels = []
        # check each hotel
        for hotel in hotels:
            # get all rooms of the hotel
            rooms = self.room_dal.get_rooms_by_hotel_id(hotel.hotel_id)
            # check each room
            for room in rooms:
                # if the room is available in the given date range
                if self.booking_dal.is_room_available(room.room_id, check_in, check_out):
                    # add hotel to result and stop checking more rooms
                    available_hotels.append(hotel)
                    break
        # return list of hotels with available rooms
        return available_hotels

    def filter_combined(self, city: str, guests: int, min_stars: int, check_in: date, check_out: date) -> list[Hotel]:
        # get hotels in the city with at least min_stars
        hotels = self.filter_by_city_and_stars(city, min_stars)
        # list to store matching hotels
        matching_hotels = []
        # check each hotel
        for hotel in hotels:
            # get all rooms for the hotel
            rooms = self.room_dal.get_rooms_by_hotel_id(hotel.hotel_id)
            # check each room
            for room in rooms:
                # get room type to check max guests
                room_type = self.room_type_dal.get_by_id(room.type_id)
                # if room fits the guests and is available
                if room_type.max_guests >= guests and self.booking_dal.is_room_available(room.room_id, check_in, check_out):
                    # add hotel to result and stop checking more rooms
                    matching_hotels.append(hotel)
                    break
        # return hotels that match all filters
        return matching_hotels
    
    def get_hotel_by_name(self, name: str) -> Hotel | None:
        # get all hotels from the database
        hotels = self.hotel_dal.get_all_hotels()
        for hotel in hotels:
            if hotel.name.lower() == name.lower():
                return hotel
        return None
    
