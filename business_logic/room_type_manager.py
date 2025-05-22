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