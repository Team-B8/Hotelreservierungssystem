class Address:
    def __init__(self, street: str, city: str, zip_code: str, address_id: int | None = None):
        if address_id is not None and not isinstance(address_id, int):
            raise ValueError("address_id muss eine ganze Zahl sein")
        if not street:
            raise ValueError("Strasse ist erforderlich")
        if not city:
            raise ValueError("Stadt ist erforderlich")
        if not zip_code:
            raise ValueError("zip_code ist erforderlich")
        
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
    
    @address_id.setter
    def address_id(self, address_id: int) -> None:
        if not isinstance(address_id, int):
            raise ValueError("address_id muss eine ganze Zahl sein")
        self.__address_id = address_id

    @street.setter
    def street(self, street: str) -> None:
        if not street:
            raise ValueError("Strasse ist erforderlich")
        if not isinstance(street, str):
            raise ValueError("Strasse muss eine Zeichenkette sein")
        self.__street = street

    @city.setter
    def city(self, city: str) -> None:
        if not city:
            raise ValueError("Stadt ist erforderlich")
        if not isinstance(city, str):
            raise ValueError("Stadt muss eine Zeichenkette sein")
        self.__city = city

    @zip_code.setter
    def zip_code(self, zip_code: str) -> None:
        if not zip_code:
            raise ValueError("zip_code ist erforderlich")
        if not isinstance(zip_code, str):
            raise ValueError("zip_code muss ein String sein")
        self.__zip_code = zip_code

    def delete_address(self) -> None:
        self.__address_id = None
        self.__street = None
        self.__city = None
        self.__zip_code = None
