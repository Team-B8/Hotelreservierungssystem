from data_access.room_dal import RoomDAL
from model.room import Room

class RoomManager:

    def __init__(self):
        self.room_dal = RoomDAL()

    def get_rooms_by_hotel_id(self, hotel_id: int) -> list[Room]:
        # return all rooms for a given hotel
        return self.room_dal.get_rooms_by_hotel_id(hotel_id)