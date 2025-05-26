from data_access.base_dal import BaseDAL
from model.facilities import Facilities

class FacilitiesDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def create(self, facility: Facilities) -> Facilities:
        sql = "INSERT INTO Facilities (facility_name) VALUES (?)"
        params = (facility.facility_name,)
        with self._connect() as conn:
            cursor = conn.execute(sql, params)
            conn.commit()
            facility._Facilities__facility_id = cursor.lastrowid
        return facility

    def get_by_id(self, facility_id: int) -> Facilities | None:
        sql = "SELECT * FROM Facilities WHERE facility_id = ?"
        with self._connect() as conn:
            cursor = conn.execute(sql, (facility_id,))
            row = cursor.fetchone()
        if row:
            return Facilities(facility_id=row["facility_id"], facility_name=row["facility_name"])
        return None

    def get_all(self) -> list[Facilities]:
        sql = "SELECT * FROM Facilities"
        with self._connect() as conn:
            cursor = conn.execute(sql)
            rows = cursor.fetchall()
        return [Facilities(facility_id=row["facility_id"], facility_name=row["facility_name"]) for row in rows]

    def delete(self, facility_id: int) -> bool:
        sql = "DELETE FROM Facilities WHERE facility_id = ?"
        with self._connect() as conn:
            cursor = conn.execute(sql, (facility_id,))
            conn.commit()
        return cursor.rowcount > 0

    def get_facilities_by_room_id(self, room_id: int) -> list[Facilities]:
        sql = "SELECT f.facility_id, f.facility_name FROM Facilities f JOIN Room_Facilities rf ON f.facility_id = rf.facility_id WHERE rf.room_id = ?"
        with self._connect() as conn:
            cursor = conn.execute(sql, (room_id,))
            rows = cursor.fetchall()
        return [Facilities(facility_id=row["facility_id"], facility_name=row["facility_name"]) for row in rows]