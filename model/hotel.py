class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, address_id: int):
        self.hotel_id = hotel_id
        self.name = name
        self.stars = stars
        self.address_id = address_id

    def __repr__(self):
        return f"Hotel(id={self.__hotel_id}, name='{self.__name}', stars={self.__stars}, address_id={self.__address_id})"

    @property
    def hotel_id(self) -> int:
        return self.__hotel_id

    @hotel_id.setter
    def hotel_id(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Hotel-ID muss ein Integer sein.")
        self.__hotel_id = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Name muss ein nicht-leerer String sein.")
        self.__name = value

    @property
    def stars(self) -> int:
        return self.__stars

    @stars.setter
    def stars(self, value: int):
        if not isinstance(value, int) or not (1 <= value <= 5):
            raise ValueError("Sterne müssen ein Integer zwischen 1 und 5 sein.")
        self.__stars = value

    @property
    def address_id(self) -> int:
        return self.__address_id

    @address_id.setter
    def address_id(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Address-ID muss ein Integer sein.")
        self.__address_id = value