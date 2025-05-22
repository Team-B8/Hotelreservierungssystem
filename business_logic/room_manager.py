from data_access.room_dal import RoomDAL
from data_access.room_type_dal import RoomTypeDAL
from data_access.facilities_dal import FacilitiesDAL
from model.room import Room
from model.room_type import RoomType
from model.facilities import Facilities

class RoomManager:

    def __init__(self):
        self.room_dal = RoomDAL()

    def get_rooms_by_hotel_id(self, hotel_id: int) -> list[Room]:
        # return all rooms for a given hotel
        return self.room_dal.get_rooms_by_hotel_id(hotel_id)