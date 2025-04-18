from data_access.base_dal import BaseDAL
from model.address import Address

class AddressDAL(BaseDAL):
    """Data access layer for the addresses table."""
    def get_by_id(self, address_id: int) -> Address:
        cursor = self.conn.execute("SELECT * FROM addresses WHERE id=?", (address_id,))
        row = cursor.fetchone()
        if row:
            return Address(**row)
        return None

    def get_all(self) -> list[Address]:
        cursor = self.conn.execute("SELECT * FROM addresses")
        rows = cursor.fetchall()
        return [Address(**row) for row in rows]

    def create(self, address: Address) -> Address:
        cursor = self.conn.execute(
            "INSERT INTO addresses (street, city, zip_code, country) VALUES (?, ?, ?, ?)",
            (address.street, address.city, address.zip_code, address.country)
        )
        self.conn.commit()
        address.id = cursor.lastrowid
        return address

    def update(self, address: Address) -> bool:
        result = self.conn.execute(
            "UPDATE addresses SET street=?, city=?, zip_code=?, country=? WHERE id=?",
            (address.street, address.city, address.zip_code, address.country, address.id)
        )
        self.conn.commit()
        return result.rowcount > 0

    def delete(self, address_id: int) -> bool:
        result = self.conn.execute("DELETE FROM addresses WHERE id=?", (address_id,))
        self.conn.commit()
        return result.rowcount > 0