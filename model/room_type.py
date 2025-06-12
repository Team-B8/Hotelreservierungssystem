class RoomType:
    def __init__(self, type_id: int, description: str, max_guests: int):
        if not isinstance(type_id, int):
            raise ValueError("type_id muss eine ganze Zahl sein.")
        if not description or not isinstance(description, str):
            raise ValueError("Eine gültige Beschreibung ist erforderlich.")
        if not isinstance(max_guests, int) or max_guests < 1:
            raise ValueError("max_guests muss eine positive ganze Zahl sein.")

        self.__type_id = type_id
        self.__description = description
        self.__max_guests = max_guests

    def __repr__(self):
        return f"RoomType(id={self.__type_id}, description='{self.__description}', max_guests={self.__max_guests})"

    @property
    def type_id(self) -> int:
        return self.__type_id

    @type_id.setter
    def type_id(self, value: int):
        if not isinstance(value, int):
            raise TypeError("room_type_id muss eine ganze Zahl sein.")
        self.__type_id = value

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        if not value or not isinstance(value, str):
            raise TypeError("description muss eine nicht leere Zeichenkette sein.")
        self.__description = value

    @property
    def max_guests(self) -> int:
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, value: int):
        if not isinstance(value, int) or value < 1:
            raise ValueError("max_guests muss eine positive ganze Zahl sein.")
        self.__max_guests = value
