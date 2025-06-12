from model.booking import Booking

class Guest:
    def __init__(self, guest_id: int | None, first_name: str, last_name: str, email: str, address_id: int):
        # Ensure values for not nullable attributes
        if guest_id is not None and not isinstance(guest_id, int):
            raise TypeError("guest_id muss eine ganze Zahl sein")
        if not first_name:
            raise ValueError("first_name ist erforderlich")
        if not isinstance(first_name, str):
            raise ValueError("first_name muss eine Zeichenkette sein")
        if not last_name:
            raise ValueError("last_name ist erforderlich")
        if not isinstance(last_name, str):
            raise ValueError("last_name muss eine Zeichenkette sein")
        if not email:
            raise ValueError("email ist erforderlich")
        if not isinstance(email, str):
            raise ValueError("email muss eine Zeichenkette sein")
        if not address_id:
            raise ValueError("address_id ist erforderlich")
        if not isinstance(address_id, int):
            raise ValueError("address_id muss eine ganze Zahl sein")

        self.__guest_id = guest_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__address_id = address_id

    def __repr__(self):
        # defines how the guest object is represented as string
        return f"Guest(id={self.__guest_id}, name={self.__first_name} {self.__last_name}, email={self.__email})"
        
    @property
    def guest_id(self) -> int:
        return self.__guest_id

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def email(self) -> str:
        return self.__email

    @first_name.setter
    def first_name(self, new_first_name):
        if not new_first_name:
            raise ValueError("first_name ist erforderlich")
        if not isinstance(new_first_name, str):
            raise ValueError("first_name muss eine Zeichenkette sein")
        self.__first_name = new_first_name

    @last_name.setter
    def last_name(self, new_last_name):
        if not new_last_name:
            raise ValueError("last_name ist erforderlich")
        if not isinstance(new_last_name, str):
            raise ValueError("last_name muss eine Zeichenkette sein")
        self.__last_name = new_last_name

    @email.setter
    def email(self, new_email):
        if not new_email:
            raise ValueError("email ist erforderlich")
        if not isinstance(new_email, str):
            raise ValueError("email muss eine Zeichenkette sein")
        self.__email = new_email

    @property
    def full_name(self) -> str:
        return f"{self.__first_name} {self.__last_name}"


    @property
    def address_id(self) -> int:
        return self.__address_id
        
    @address_id.setter
    def address_id(self, new_address_id: int):
        if new_address_id is not None and not isinstance(new_address_id, int):
            raise TypeError("Address ID muss eine ganze Zahl sein")
        self.__address_id = new_address_id
