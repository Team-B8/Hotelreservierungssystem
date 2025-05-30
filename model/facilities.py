class Facilities:
    def __init__(self, facility_name: str, facility_id: int = None):
        # Validate inputs immediately
        if not facility_name:
            raise ValueError("facility_name is required")
        if not isinstance(facility_name, str):
            raise ValueError("facility_name must be a string")

        self.__facility_id = facility_id
        self.__facility_name = facility_name
        self.__is_deleted = False
        self.__rooms = []  # list of Room objects using this facility

    def __repr__(self):
        # Textual representation of the facility object
        return f"Facility(id={self.__facility_id}, name={self.__facility_name})"

    @property
    def facility_id(self):
        return self.__facility_id

    @property
    def facility_name(self):
        return self.__facility_name

    @facility_name.setter
    def facility_name(self, new_facility_name):
        if not new_facility_name:
            raise ValueError("facility_name is required")
        if not isinstance(new_facility_name, str):
            raise ValueError("facility_name must be a string")
        self.__facility_name = new_facility_name

    @property
    def rooms(self):
        return self.__rooms

    def assign_to_room(self, room):
        # Adds the room to the facility if not already assigned
        if room not in self.__rooms:
            self.__rooms.append(room)

    def delete_facility(self):
        if not self.__is_deleted:
            self.__is_deleted = True
            print(f"Facility {self.__facility_name} was marked as deleted.")
        else:
            print(f"Facility {self.__facility_name} is already deleted.")

    @property
    def is_deleted(self):
        return self.__is_deleted

    def restore(self):
        if self.__is_deleted:
            self.__is_deleted = False
            print(f"Facility {self.__facility_name} was restored.")
        else:
            print(f"Facility {self.__facility_name} is already active.")
