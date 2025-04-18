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
        return self.dal.get_by_id(facility_id)

    def delete_facility(self, facility_id: int) -> bool:
        return self.dal.delete(facility_id)

