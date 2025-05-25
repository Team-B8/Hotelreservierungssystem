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

    def get_rooms_by_hotel_id(self, hotel_id: int) -> list[Room]:
        # return all rooms for a given hotel
        return self.room_dal.get_rooms_by_hotel_id(hotel_id)

    # dictionary to structure and return all relevant room info
    def get_detailed_rooms_by_hotel_id(self, hotel_id: int, nights: int = 1) -> list[dict]:
        # fetch rooms for the hotel
        rooms = self.room_dal.get_rooms_by_hotel_id(hotel_id)
        detailed_rooms = []
        for room in rooms:
            # get room type info
            room_type = self.room_type_dal.get_by_id(room.type_id)
            # get facilities
            facilities = self.facilities_dal.get_by_room_id(room.room_id)
            facility_names = [f.facility_name for f in facilities]
            # build a detailed dict
            detailed_rooms.append({
                "room_id": room.room_id,
                "room_no": room.room_no,
                "type_description": room_type.description,
                "max_guests": room_type.max_guests,
                "facilities": facility_names,
                "price_per_night": room.price_per_night,
                "total_price": round(room.price_per_night * nights, 2)
            })
        return detailed_rooms
    

    def get_available_rooms_by_hotel_and_dates(self, hotel_id: int, check_in_date: str, check_out_date: str) -> list[Room]:
        # Get all rooms for the hotel
        all_rooms = self.room_dal.get_rooms_by_hotel_id(hotel_id)
        # Get all room_ids that are already booked during the specified dates
        booked_room_ids = self.room_dal.get_booked_room_ids(hotel_id, check_in_date, check_out_date)
        # Return only those rooms that are not booked
        available_rooms = [room for room in all_rooms if room.room_id not in booked_room_ids]
        return available_rooms