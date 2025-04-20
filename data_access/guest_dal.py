# guest_dal.py (Data Access Layer)
from data_access.base_dal import BaseDAL
from model.guest import Guest

class GuestDAL(BaseDAL):
    def __init__(self, db_path="hotel.db"):
        super().__init__(db_path)  # calls the constructor of BaseDAL to set up the DB connection

    def create(self, guest: Guest) -> Guest:
        # Inserts a new guest into the database
        sql = "INSERT INTO guests (first_name, last_name, email) VALUES (?, ?, ?)"
        params = (guest.first_name, guest.last_name, guest.email)
        last_row_id, _ = self.execute(sql, params)
        guest._Guest__guest_id = last_row_id  # sets the guest ID after insertion (name mangling safe)
        return guest

    def get_by_id(self, guest_id: int) -> Guest | None:
        # Retrieves a guest by their ID
        sql = "SELECT * FROM guests WHERE id = ?"
        row = self.fetchone(sql, (guest_id,))
        if row:
            return Guest(guest_id=row["id"], first_name=row["first_name"], last_name=row["last_name"], email=row["email"])
        return None

    def get_by_email(self, email: str) -> Guest | None:
        # Retrieves a guest by their email address
        sql = "SELECT * FROM guests WHERE email = ?"
        row = self.fetchone(sql, (email,))
        if row:
            return Guest(guest_id=row["id"], first_name=row["first_name"], last_name=row["last_name"], email=row["email"])
        return None

    def delete(self, guest_id: int) -> bool:
        # Physically deletes a guest by their ID from the database (not just logical)
        sql = "DELETE FROM guests WHERE id = ?"
        _, row_count = self.execute(sql, (guest_id,))
        return row_count > 0

