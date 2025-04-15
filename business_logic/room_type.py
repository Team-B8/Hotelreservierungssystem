

class RoomType:

    def __init__(self, room_type_id: int, description: str, max_guests: int):

        if not room_type_id:
            raise ValueError("Room type id required")
        if not isinstance(room_type_id, int):
            raise ValueError("Room type id must be an integer")
        if not description:
            raise ValueError("A descrition is required")
        if not isinstance(description, str):
            raise ValueError("The description must be a string")
        if not max_guests:
            raise ValueError("Maximum guest capacity required")
        if not isinstance(max_guests, int):
            raise ValueError("Maximum guest capacity must be an integer")

    self.__room_type_id: int = room_type_id
    self.__description: str = description
    self.__max_guests: int = max_guests

    def __repr__(self):
        return f"Room type id: {room_type_id}\nRoom type description: {description}\nMaximum guest capacity: {max_guest}"


#Getter
    @property
    def room_type_id(self):
        return self.__room_type_id

    @property
    def description(self):
        return self.__description

    @property
    def max_guests(self):
        return self.__max_guests

#Setter