from data_access.base_dal import BaseDAL
from model.address import Address

class AddressDAL(BaseDAL):
    def __init__(self):
        super().__init__()
        
    def get_by_id(self, address_id: int) -> Address | None:
        with self._connect() as conn:
            cursor = conn.execute("SELECT * FROM address WHERE address_id = ?", (address_id,))
            row = cursor.fetchone()
        return Address(**row) if row else None

    def get_all_addresses(self) -> list[Address]:
        with self._connect() as conn:
            cursor = conn.execute("SELECT * FROM address")
            rows = cursor.fetchall()
        return [Address(**row) for row in rows]

    def create(self, address: Address) -> Address:
        with self._connect() as conn:
            cursor = conn.execute(
                "INSERT INTO address (street, city, zip_code) VALUES (?, ?, ?)",
                (address.street, address.city, address.zip_code)
            )
            conn.commit()
            address.address_id = cursor.lastrowid
        return address

    def update_address(self, address: Address) -> bool:
        # connect to the database and run the update query
        with self._connect() as conn:
            result = conn.execute(
                # SQL query to update the address fields
                "UPDATE address SET street = ?, city = ?, zip_code = ? WHERE address_id = ?",
                (address.street, address.city, address.zip_code, address.address_id)
            )
            conn.commit()
        # return True if at least one row was updated
        return result.rowcount > 0

    def delete(self, address_id: int) -> bool:
        with self._connect() as conn:
            result = conn.execute("DELETE FROM address WHERE address_id = ?", (address_id,))
            conn.commit()
        return result.rowcount > 0

    def get_address_by_hotel(self, hotel_id: int) -> Address | None:
        with self._connect() as conn:
            cursor = conn.execute(
                "SELECT a.* FROM address a JOIN hotel h ON a.address_id = h.address_id WHERE h.hotel_id = ?",
                (hotel_id,)
            )
            row = cursor.fetchone()
        return Address(**row) if row else None

    def get_address_by_guest(self, guest_id: int) -> Address | None:
        with self._connect() as conn:
            cursor = conn.execute(
                "SELECT a.* FROM address a JOIN guest g ON a.address_id = g.address_id WHERE g.guest_id = ?",
                (guest_id,)
            )
            row = cursor.fetchone()
        return Address(**row) if row else None