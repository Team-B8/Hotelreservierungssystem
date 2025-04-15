from data_access.base_dal import BaseDal
from model.address import Address

class AddressDAL(BaseDal):
    def create_address(self, street: str, city: str, zip_code: str) -> Address:
        sql = "INSERT INTO Address (street, city, zip_code) VALUES (?, ?, ?)"
        params = (street, city, zip_code)
        last_id, _ = self.execute(sql, params)
        return Address(last_id, street, city, zip_code)

    def get_address_by_id(self, address_id: int) -> Address | None:
        sql = "SELECT address_id, street, city, zip_code FROM Address WHERE address_id = ?"
        result = self.fetchone(sql, (address_id,))
        if result:
            return Address(*result)
        return None

    def delete_address(self, address_id: int) -> None:
        sql = "DELETE FROM Address WHERE address_id = ?"
        self.execute(sql, (address_id,))
