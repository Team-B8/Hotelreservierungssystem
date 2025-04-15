class Address:
    def __init__(self, address_id: int, street: str, city: str, zip_code: str):
        self.__address_id = address_id
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code

    def get_address_id(self) -> int:
        return self.__address_id

    def get_street(self) -> str:
        return self.__street

    def get_city(self) -> str:
        return self.__city

    def get_zip_code(self) -> str:
        return self.__zip_code

    def set_street(self, street: str) -> None:
        self.__street = street

    def set_city(self, city: str) -> None:
        self.__city = city

    def set_zip_code(self, zip_code: str) -> None:
        self.__zip_code = zip_code

    def get_full_address(self) -> str:
        return f"{self.__street}, {self.__zip_code} {self.__city}"

    def __repr__(self):
        return f"Address({self.__address_id}, {self.__street}, {self.__city}, {self.__zip_code})"
