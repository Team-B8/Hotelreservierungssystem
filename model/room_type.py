class RoomType:
    def __init__(self, room_type_id: int, description: str, max_guests: int):
        if not isinstance(room_type_id, int):
            raise ValueError("room_type_id must be an integer.")
        if not description or not isinstance(description, str):
            raise ValueError("A valid description is required.")
        if not isinstance(max_guests, int) or max_guests < 1:
            raise ValueError("max_guests must be a positive integer.")

        self.__room_type_id = room_type_id
        self.__description = description
        self.__max_guests = max_guests

    def __repr__(self):
        return (
            f"RoomType(id={self.__room_type_id}, "
            f"description='{self.__description}', "
            f"max_guests={self.__max_guests})"
        )

    @property
    def room_type_id(self) -> int:
        return self.__room_type_id

    @room_type_id.setter
    def room_type_id(self, value: int):
        if not isinstance(value, int):
            raise TypeError("room_type_id must be an integer.")
        self.__room_type_id = value

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        if not value or not isinstance(value, str):
            raise TypeError("description must be a non-empty string.")
        self.__description = value

    @property
    def max_guests(self) -> int:
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, value: int):
        if not isinstance(value, int) or value < 1:
            raise ValueError("max_guests must be a positive integer.")
        self.__max_guests = value