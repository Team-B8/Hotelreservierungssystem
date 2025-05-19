from data_access.base_dal import BaseDAL
from model.address import Address

class AddressDAL(BaseDAL):
    def __init__(self):
        super().__init__()
        
    def get_by_id(self, address_id: int) -> Address | None:
        cursor = self.conn.execute("SELECT * FROM address WHERE address_id = ?", (address_id,))
        row = cursor.fetchone()
        return Address(**row) if row else None

    def get_all_addresses(self) -> list[Address]:
        cursor = self.conn.execute("SELECT * FROM address")
        rows = cursor.fetchall()
        return [Address(**row) for row in rows]

    def create(self, address: Address) -> Address:
        cursor = self.conn.execute(
            "INSERT INTO address (street, city, zip_code) VALUES (?, ?, ?)",
            (address.street, address.city, address.zip_code)
        )
        self.conn.commit()
        address.id = cursor.lastrowid
        return address

    def update(self, address: Address) -> bool:
        result = self.conn.execute(
            "UPDATE address SET street = ?, city = ?, zip_code = ? WHERE address_id = ?",
            (address.street, address.city, address.zip_code, address.id)
        )
        self.conn.commit()
        return result.rowcount > 0

    def delete(self, address_id: int) -> bool:
        result = self.conn.execute("DELETE FROM address WHERE address_id = ?", (address_id,))
        self.conn.commit()
        return result.rowcount > 0

    def get_address_by_hotel(self, hotel_id: int) -> Address | None:
        cursor = self.conn.execute(
            "SELECT a.* FROM address a JOIN hotel h ON a.address_id = h.address_id WHERE h.hotel_id = ?",
            (hotel_id,)
        )
        row = cursor.fetchone()
        return Address(**row) if row else None

    def get_address_by_guest(self, guest_id: int) -> Address | None:
        cursor = self.conn.execute(
            "SELECT a.* FROM address a JOIN guest g ON a.address_id = g.address_id WHERE g.guest_id = ?",
            (guest_id,)
        )
        row = cursor.fetchone()
        return Address(**row) if row else None