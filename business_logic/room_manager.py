from data_access.room_dal import RoomDAL
from data_access.room_type_dal import RoomTypeDAL
from data_access.facilities_dal import FacilitiesDAL
from model.room import Room
from model.room_type import RoomType
from model.facilities import Facilities

class RoomManager:

    def __init__(self):
        self.room_dal = RoomDAL()
        self.room_type_dal = RoomTypeDAL()
        self.facilities_dal = FacilitiesDAL()

    def get_room_by_id(self, room_id: int) -> Room:
        return self.room_dal.get_by_id(room_id)

    def get_rooms_by_hotel_id(self, hotel_id: int) -> list[Room]:
        # return all rooms for a given hotel
        return self.room_dal.get_rooms_by_hotel_id(hotel_id)
    
    def get_available_rooms_by_hotel_and_dates(self, hotel_id: int, check_in_date: str, check_out_date: str) -> list[Room]:
        # Get all rooms for the hotel
        all_rooms = self.room_dal.get_rooms_by_hotel_id(hotel_id)
        # Get all room_ids that are already booked during the specified dates
        booked_room_ids = self.room_dal.get_booked_room_ids(hotel_id, check_in_date, check_out_date)
        # Return only those rooms that are not booked
        available_rooms = [room for room in all_rooms if room.room_id not in booked_room_ids]
        return available_rooms
    
    def get_detailed_available_rooms(self, hotel_id: int, check_in: str, check_out: str) -> list[Room]:
        # Returns all available rooms for the hotel in the given date range
        all_rooms = self.get_rooms_by_hotel_id(hotel_id)
        available_rooms = self.get_available_rooms_by_hotel_and_dates(hotel_id, check_in, check_out)
        # Create a mapping of room_id to Room for fast lookup
        room_dict = {room.room_id: room for room in all_rooms}
        # Return only Room objects for the available room_ids
        return [room_dict[room.room_id] for room in available_rooms if room.room_id in room_dict]
    
    def create_room(self, hotel_id: int, type_id: int, price_per_night: float) -> Room:
        # get the next available room number for the hotel
        room_no = self.room_dal.get_next_room_number(hotel_id)
        # create a new room in the database and get its ID
        room_id = self.room_dal.create_room(hotel_id, room_no, type_id, price_per_night)
        # return a new Room object with the given data
        return Room(room_id=room_id, hotel_id=hotel_id, room_no=room_no, type_id=type_id, price_per_night=price_per_night)
    
    def get_all_rooms_with_facilities(self) -> list[dict]:
        # call function from data access layer
        return self.room_dal.get_rooms_with_facilities()
    
    def update_room_price(self, room_id: int, new_price: float) -> bool:
        # update the room price using the DAL
        return self.room_dal.update_price(room_id, new_price)