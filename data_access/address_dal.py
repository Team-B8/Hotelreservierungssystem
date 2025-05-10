from data_access.base_dal import BaseDAL
from model.address import Address

class AddressDAL(BaseDAL):
    def get_by_id(self, address_id: int) -> Address:
        params = tuple([address_id])
        cursor = self.conn.execute("SELECT * FROM address WHERE id=?", params)
        row = cursor.fetchone()
        if row:
            return Address(**row)
        return None

    def get_all_address(self) -> list[Address]:
        cursor = self.conn.execute("SELECT * FROM address")
        rows = cursor.fetchall()
        return [Address(**row) for row in rows]

    def create(self, address: Address) -> Address:
        cursor = self.conn.execute(
            "INSERT INTO address (street, city, zip_code, country) VALUES (?, ?, ?, ?)",
            (address.street, address.city, address.zip_code, address.country)
        )
        self.conn.commit()
        address.id = cursor.lastrowid
        return address

    def update(self, address: Address) -> bool:
        result = self.conn.execute(
            "UPDATE address SET street=?, city=?, zip_code=?, country=? WHERE id=?",
            (address.street, address.city, address.zip_code, address.country, address.id)
        )
        self.conn.commit()
        return result.rowcount > 0

    def delete(self, address_id: int) -> bool:
        result = self.conn.execute("DELETE FROM address WHERE id=?", (address_id,))
        self.conn.commit()
        return result.rowcount > 0
    
    def get_address_by_hotel(self, address)

    def get_address_by_guest(self)