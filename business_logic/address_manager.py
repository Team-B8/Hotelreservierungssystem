from data_access.address_dal import AddressDAL
from model.address import Address

class AddressManager:
    def __init__(self):
        # Input of the data access layer for addresses
        self.__address_dal = AddressDAL()

    def create_address(self, street: str, city: str, zip_code: str) -> Address:
        # Create and save a new address with the given details
        address = Address(street=street, city=city, zip_code=zip_code)
        return self.__address_dal.create(address)

