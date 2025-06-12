class Facilities:
    def __init__(self, facility_name: str, facility_id: int = None):
        # Validate inputs immediately
        if not facility_name:
            raise ValueError("facility_name ist erforderlich")
        if not isinstance(facility_name, str):
            raise ValueError("facility_name muss eine Zeichenkette sein")

        self.__facility_id = facility_id
        self.__facility_name = facility_name
        self.__is_deleted = False
        self.__rooms = []

    def __repr__(self):
        return f"Facility(id={self.__facility_id}, name={self.__facility_name})"

    @property
    def facility_id(self):
        return self.__facility_id
    
    @facility_id.setter
    def facility_id(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Facility-ID muss eine ganze Zahl sein")
        self.__facility_id = value

    @property
    def facility_name(self):
        return self.__facility_name

    @facility_name.setter
    def facility_name(self, new_facility_name):
        if not new_facility_name:
            raise ValueError("facility_name ist erforderlich")
        if not isinstance(new_facility_name, str):
            raise ValueError("facility_name muss eine Zeichenkette sein")
        self.__facility_name = new_facility_name

    @property
    def rooms(self):
        return self.__rooms

    def assign_to_room(self, room):
        if room not in self.__rooms:
            self.__rooms.append(room)

    def delete_facility(self):
        if not self.__is_deleted:
            self.__is_deleted = True
            print(f"Facility {self.__facility_name} wurde als gelöscht markiert.")
        else:
            print(f"Facility {self.__facility_name} ist bereits gelöscht.")

    @property
    def is_deleted(self):
        return self.__is_deleted
