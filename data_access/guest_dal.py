# guest_dal.py (Data Access Layer)
from data_access.base_dal import BaseDAL
from model.guest import Guest

class GuestDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def create(self, guest: Guest) -> Guest:
        # Inserts a new guest into the database
        sql = "INSERT INTO Guest (first_name, last_name, email, address_id) VALUES (?, ?, ?, ?)"
        params = (guest.first_name, guest.last_name, guest.email, guest.address_id)
        with self._connect() as conn:
            cursor = conn.execute(sql, params)
            conn.commit()
            guest._Guest__guest_id = cursor.lastrowid
        return guest

    def get_by_id(self, guest_id: int) -> Guest | None:
        # Retrieves a guest by their ID
        sql = "SELECT * FROM Guest WHERE guest_id = ?"
        with self._connect() as conn:
            cursor = conn.execute(sql, (guest_id,))
            row = cursor.fetchone()
        if row:
            return Guest(guest_id=row["guest_id"], first_name=row["first_name"], last_name=row["last_name"], email=row["email"])
        return None

    def get_by_email(self, email: str) -> Guest | None:
        # Retrieves a guest by their email address
        sql = "SELECT * FROM Guest WHERE email = ?"
        with self._connect() as conn:
            cursor = conn.execute(sql, (email,))
            row = cursor.fetchone()
        if row:
            return Guest(guest_id=row["guest_id"], first_name=row["first_name"], last_name=row["last_name"], email=row["email"], address_id=row["address_id"])
        return None

    def delete(self, guest_id: int) -> bool:
        # Physically deletes a guest by their ID from the database (not just logical)
        sql = "DELETE FROM Guest WHERE id = ?"
        with self._connect() as conn:
            cursor = conn.execute(sql, (guest_id,))
            conn.commit()
        return cursor.rowcount > 0
