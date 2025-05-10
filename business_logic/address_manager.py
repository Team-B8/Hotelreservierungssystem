from data_access.address_dal import AddressDAL
from model.address import Address

class AddressManager:
    def __init__(self):
        # Initialize the data access layer for addresses
        self.__address_dal = AddressDAL()

    def create_address(self, street: str, city: str, zip_code: str) -> Address:
        # Create and save a new address with the given details
        return self.__address_dal.create_address(street, city, zip_code)

    def get_address(self, address_id: int) -> Address | None:
        # Retrieve an address by its ID
        return self.__address_dal.get_address_by_id(address_id)

    def delete_address(self, address_id: int) -> None:
        # Delete the address with the given ID
        self.__address_dal.delete_address(address_id)
