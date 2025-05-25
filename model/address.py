class Address:
    def __init__(self, address_id: int | None, street: str, city: str, zip_code: str):
        if address_id is not None and not isinstance(address_id, int):
            raise ValueError("address_id must be an integer")
        if not street:
            raise ValueError("street is required")
        if not city:
            raise ValueError("city is required")
        if not zip_code:
            raise ValueError("zip_code is required")
        
        self.__address_id = address_id
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code

    def __repr__(self):
        return f"Address({self.__address_id}, {self.__street}, {self.__city}, {self.__zip_code})"

    @property
    def address_id(self) -> int:
        return self.__address_id
    
    @property
    def street(self) -> str:
        return self.__street

    @property
    def city(self) -> str:
        return self.__city

    @property
    def zip_code(self) -> str:
        return self.__zip_code  
    
    def get_full_address(self) -> str:
        return f"{self.__street}, {self.__city}, {self.__zip_code}"

    @street.setter
    def street(self, street: str) -> None:
        if not street:
            raise ValueError("street is required")
        if not isinstance(street, str):
            raise ValueError("street must be a string")
        self.__street = street

    @city.setter
    def city(self, city: str) -> None:
        if not city:
            raise ValueError("city is required")
        if not isinstance(city, str):
            raise ValueError("city must be a string")
        self.__city = city

    @zip_code.setter
    def zip_code(self, zip_code: str) -> None:
        if not zip_code:
            raise ValueError("zip_code is required")
        if not isinstance(zip_code, str):
            raise ValueError("zip_code must be a string")
        self.__zip_code = zip_code