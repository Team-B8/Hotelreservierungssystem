from business_logic.room import Room

class Facilities:
    """
    Model Class Facilities
    """
    def __init__(self, facility_id: int, facility: str):

#Input Validation
        if not facility_id:
            raise ValueError("ID is required")
        if not isinstance(facility_id, int):
            raise ValueError("ID must be integer")
        if not facility:
            raise ValueError("Facility is required")
        if not isinstance(facility, str):
            raise ValueError("Facility must be a string")
    
#Initialization: Facility ID, Name
    self.__facility_id = facility_id
    self.__facility: str = facility
    self.__room_no: Rooms int = [] #How should the relation be set???

#Formatted representation of class
    def __repr__(self):
        return f"Facility(id={self.__facility_id}, name={self.__name})"

#Getter
    @property
    def facility_id(self) -> int:
        return self.__facility_id


    @property 
    def name(self) -> int:
        return self.__facility

### Braucht es so viele setter wann macht es sinn?
#Setter
    @facility_id.setter
    def facility_id(self, facility_id):
        if not facility_id:
            raise ValueError("ID is required")
        if not isinstance(facility_id, int):
            raise ValueError("ID must be integer")
        self.__facility_id = facility_id

    @facility.setter
    def facility(self, facility) -> None:
        if not name:
            raise ValueError("Name is required")
        if not isinstance(facility, str):
            raise ValueError("Name must be a string")
        self.__facility = facility

