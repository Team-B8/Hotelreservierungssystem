from data_access.facilities_dal import FacilitiesDAL
from model.facilities import Facilities

class FacilitiesManager:
    def __init__(self):
        self.dal = FacilitiesDAL()

    def add_facility(self, facility_name: str) -> Facilities:
        # Adds a facility only if it doesn't already exist
        existing = [f for f in self.dal.get_all() if f.facility_name == facility_name]
        if existing:
            print("Facility already exists.")
            return existing[0]
        new_facility = Facilities(facility_name, None)
        return self.dal.create(new_facility)

    def get_facility_by_id(self, facility_id: int) -> Facilities | None:
        # Get a facility by its ID
        return self.dal.get_by_id(facility_id)

    def delete_facility(self, facility_id: int) -> bool:
        # Delete a facility by its ID
        return self.dal.delete(facility_id)

    def get_facilities_for_room(self, room_id: int):
        # Get all facilities assigned to a specific room
        return self.dal.get_facilities_by_room_id(room_id)
    
    def update_facility(self, facility_id: int, new_name: str) -> bool:
        # Update the facility name in the database
        return self.dal.update(facility_id, new_name)
    
    def get_all_facilities(self):
        # Get all facilities from the database
        return self.dal.get_all()
