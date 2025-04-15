# 

from business_logic.facilities import Facilities

class Room:
    """
    Model Class Room
    """

    def __init__(self, room_id: int, room_no: int, price_per_night: float)

# Input Validation -> reacts to certain types of possible false inputs with a helping response
        if not room_id:
            raise ValueError("album_id is required")
        if not isinstance(album_id, int):
            raise ValueError("album_ide must be an integer")
        if not room_no:
            raise ValueError("room_no is required")
        if not isinstance(room_no, int):
            raise ValueError("room_no must be an integer")
        if not price_per_night:
            raise ValueError("price_per_night is required")

# Attribute initialization: ID, No, Price

        self.__room_id: int = room_id
        self.__room_no: int = room_no
        self.__price_per_night: float = price_per_night
        self.__facility: int = []

    def __repr__(self): #Format in which whole object is represented -> __repr__
        return (f"Room Id = {self.__room_id}, Room No. = {self.__room_no}, Price per night: {self.__price_per_night}")

#Getter for each variable with use of decorators
    @property
    def room_id(self) -> int:
        return self.__room_id

    @property
    def room_no(self) -> int:
        return self.__room_no
    
    @property
    def price_per_night(self) -> float:
        return self.__price_per_night

#Setter for each variable with use of decorators
    @room_id.setter
    def room_id(self, room_id: int) -> None:
        if not room_id:
            raise ValueError("ID is required")
        if not isinstance(room_id, int)
            raise ValueError("ID must me an integer")
        self.__room_id = room_id

    @room_no.setter
    def room_no(self, room_no: int) -> None:
        if not room_no:
            raise ValueError("No. is required")
        if not isinstance(room_id, int)
            raise ValueError("No. must me an integer")
        self.__room_no = room_no

    @price_per_night.setter
    def price_per_night(self, price_per_night: int) -> None:
        if not price_per_night:
            raise ValueError("Price per night is required")
        if not isinstance(price_per_night, float):
            raise ValueError("Price per night must be a float")
    self.__price_per_night = price_per_night

#Adding a facility
    def add_facility(self, facility):
        if facility not in self.__facility:
            self.__facility.append(facility)
        facilities.room = self


## Mit Hotel verbunden. Hotel soll Room hinzufügen können als auch entfernen.









