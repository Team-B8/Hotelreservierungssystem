class Facilities:
    def __init__(self, facility_id: int, facility_name: str):
        self._facility_id = facility_id
        self._facility_name = facility_name
        self._is_deleted = False

    @property
    def facility_id(self):
        return self._facility_id

    @property
    def facility_name(self):
        return self._facility_name

    @facility_name.setter
    def facility_name(self, new_facility_name):
        if self._facility_name != new_facility_name:
            self._facility_name = new_facility_name
        else:
            print(f"The new facility name is the same as the one before")

    def delete_facility(self):
        if not self._is_deleted:
            self._is_deleted = True
            print(f"Facility {self.facility_name} was marked as deleted.")
        else:
            print(f"Facility {self.facility_name} is already deleted.")
            
    @property
    def is_deleted(self):
        return self._is_deleted

    def restore(self):
        if self._is_deleted:
            self._is_deleted = False
            print(f"{self._first_name} {self._last_name} was restored.")
        else:
            print(f"{self._first_name} {self._last_name} is already active.")
