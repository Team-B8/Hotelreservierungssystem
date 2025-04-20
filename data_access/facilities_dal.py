# facilities_dal.py (Data Access Layer)
from data_access.base_dal import BaseDAL
from model.facilities import Facilities

class FacilitiesDAL(BaseDAL):
    def __init__(self, db_path="hotel.db"):
        super().__init__(db_path)  # sets up DB connection via BaseDAL

    def create(self, facility: Facilities) -> Facilities:
        # Inserts a new facility into the database
        sql = "INSERT INTO facilities (facility_name) VALUES (?)"
        params = (facility.facility_name,)
        last_row_id, _ = self.execute(sql, params)
        facility._Facilities__facility_id = last_row_id  # assign DB-generated ID
        return facility

    def get_by_id(self, facility_id: int) -> Facilities | None:
        # Retrieves a facility by its ID
        sql = "SELECT * FROM facilities WHERE id = ?"
        row = self.fetchone(sql, (facility_id,))
        if row:
            return Facilities(facility_id=row["id"], facility_name=row["facility_name"])
        return None

    def get_all(self) -> list[Facilities]:
        # Retrieves all facilities from the database
        sql = "SELECT * FROM facilities"
        rows = self.fetchall(sql)
        return [Facilities(facility_id=row["id"], facility_name=row["facility_name"]) for row in rows]

    def delete(self, facility_id: int) -> bool:
        # Deletes a facility by its ID
        sql = "DELETE FROM facilities WHERE id = ?"
        _, row_count = self.execute(sql, (facility_id,))
        return row_count > 0
