class Room:
    def __init__(self, room_id: int, hotel_id: int, room_no: str, type_id: int, price_per_night: float):
        self.room_id = room_id
        self.hotel_id = hotel_id
        self.room_no = room_no
        self.type_id = type_id
        self.price_per_night = price_per_night
        self.__room_type = None
        self.__facilities = []

    def __repr__(self):
        return f"Room(id={self.__room_id}, hotel_id={self.__hotel_id}, number='{self.__room_no}', type_id={self.__type_id}, price={self.__price_per_night})"

    @property
    def room_id(self) -> int:
        return self.__room_id

    @room_id.setter
    def room_id(self, value: int):
        if not isinstance(value, int):
            raise TypeError("room_id must be an integer")
        self.__room_id = value

    @property
    def hotel_id(self) -> int:
        return self.__hotel_id

    @hotel_id.setter
    def hotel_id(self, value: int):
        if not isinstance(value, int):
            raise TypeError("hotel_id must be an integer")
        self.__hotel_id = value

    @property
    def room_no(self) -> str:
        return self.__room_no

    @room_no.setter
    def room_no(self, value: str):
        if not isinstance(value, str):
            raise TypeError("room_no must be a string")
        self.__room_no = value

    @property
    def type_id(self) -> int:
        return self.__type_id

    @type_id.setter
    def type_id(self, value: int):
        if not isinstance(value, int):
            raise TypeError("type_id must be an integer")
        self.__type_id = value

    @property
    def price_per_night(self) -> float:
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("price_per_night must be numeric")
        self.__price_per_night = float(value)
    
    @property
    def room_type(self):
        return self.__room_type

    @room_type.setter
    def room_type(self, room_type_obj):
        self.__room_type = room_type_obj

    @property
    def facilities(self):
        return self.__facilities

    def add_facility(self, facility_obj):
        if facility_obj not in self.__facilities:
            self.__facilities.append(facility_obj)