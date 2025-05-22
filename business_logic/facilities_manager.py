# facilities_manager.py (Business Logic Layer)
from data_access.facilities_dal import FacilitiesDAL
from model.facilities import Facilities

class FacilitiesManager:
    def __init__(self):
        self.dal = FacilitiesDAL()  # connects to the DAL layer

    def add_facility(self, facility_name: str) -> Facilities:
        # Adds a facility only if it doesn't already exist
        existing = [f for f in self.dal.get_all() if f.facility_name == facility_name]
        if existing:
            print("Facility already exists.")
            return existing[0]
        new_facility = Facilities(None, facility_name)
        return self.dal.create(new_facility)

    def get_facility_by_id(self, facility_id: int) -> Facilities | None:
        # Get a facility by its ID
        return self.dal.get_by_id(facility_id)

    def delete_facility(self, facility_id: int) -> bool:
        # Delete a facility by its ID
        return self.dal.delete(facility_id)

    def assign_facility_to_room(self, facility: Facilities, room):
        # Assigns the facility to the room bidirectionally
        facility.assign_to_room(room)
        room.add_facility(facility)

    def get_facilities_by_room_id(self, room_id: int) -> list[Facilities]:
        # Get all facilities assigned to a specific room
        return self.dal.get_facilities_by_room_id(room_id)