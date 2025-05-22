from data_access.base_dal import BaseDAL
from model.facilities import Facilities

class FacilitiesDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def create(self, facility: Facilities) -> Facilities:
        # Inserts a new facility into the database
        sql = "INSERT INTO Facilities (facility_name) VALUES (?)"
        params = (facility.facility_name,)
        last_row_id, _ = self.execute(sql, params)
        facility._Facilities__facility_id = last_row_id  # assign DB-generated ID
        return facility

    def get_by_id(self, facility_id: int) -> Facilities | None:
        # Retrieves a facility by its ID
        sql = "SELECT * FROM Facilities WHERE facility_id = ?"
        row = self.fetchone(sql, (facility_id,))
        if row:
            return Facilities(facility_id=row["facility_id"], facility_name=row["facility_name"])
        return None

    def get_all(self) -> list[Facilities]:
        # Retrieves all facilities from the database
        sql = "SELECT * FROM Facilities"
        rows = self.fetchall(sql)
        return [Facilities(facility_id=row["facility_id"], facility_name=row["facility_name"]) for row in rows]

    def delete(self, facility_id: int) -> bool:
        # Deletes a facility by its ID
        sql = "DELETE FROM Facilities WHERE facility_id = ?"
        _, row_count = self.execute(sql, (facility_id,))
        return row_count > 0

    def get_facilities_by_room_id(self, room_id: int) -> list[Facilities]:
        # SQL query to get all facilities for a given room using a JOIN
        sql = "SELECT f.facility_id, f.facility_name FROM Facilities f JOIN Room_Facilities rf ON f.facility_id = rf.facility_id WHERE rf.room_id = ?"
        # get all matching rows from the database
        rows = self.fetchall(sql, (room_id,))
        # convert each row to a Facilities object and return the list
        return [Facilities(facility_id=row["facility_id"], facility_name=row["facility_name"]) for row in rows]