from data_access.room_type_dal import RoomTypeDAL
from model.room_type import RoomType

class RoomTypeManager:
    def __init__(self):
        self.dal = RoomTypeDAL()

    def get_by_id(self, type_id: int) -> RoomType | None:
        # Returns a single RoomType by its ID
        return self.dal.get_by_id(type_id)

    def get_all(self) -> list[RoomType]:
        # Returns a list of all RoomTypes
        return self.dal.get_all()
    
    def create_room_type(self, description: str, max_guests: int) -> RoomType:
        # create a new room type using the data access layer
        return self.dal.create_room_type(description, max_guests)

    def update_room_type(self, type_id: int, new_description: str, new_max_guests: int) -> bool:
        # update an existing room type by ID
        return self.dal.update_room_type(type_id, new_description, new_max_guests)

    def delete_room_type(self, type_id: int) -> bool:
        # delete a room type by ID
        return self.dal.delete_room_type(type_id)
    
    def is_type_in_use(self, type_id: int) -> bool:
        # check via data access if this room type is used by any room
        return self.dal.is_type_in_use(type_id)