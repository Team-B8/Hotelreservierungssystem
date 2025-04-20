import model
from model.booking import Booking

class Guest:
    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str):
        # Ensure values for not nullable attributes
        if not guest_id:
            raise ValueError("guest_id is required")
        if not isinstance(genre_id, int):
            raise ValueError("guest_id must be an integer")
        if not first_name:
            raise ValueError("first_name is required")
        if not last_name:
            raise ValueError("last_name is required")
        if not email:
            raise ValueError("email is required")
        if not isinstance(first_name, str):
            raise ValueError("first_name must be an string")
        if not isinstance(last_name, str):
            raise ValueError("last_name must be an string")
        if not isinstance(email, str):
            raise ValueError("email must be an string")
   

        self._guest_id = guest_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__bookings = []  # list to store associated bookings
        self.__is_deleted = False  # flag to mark logical deletion

    def __repr__(self):
        # defines how the guest object is represented as string
        return f"Guest(id={self._guest_id}, name={self.__first_name} {self.__last_name}, email={self.__email})"
        
    @property
    def guest_id(self):
        return self.__guest_id

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email(self):
        return self.__email

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, new_first_name):
        if not new_first_name:
            raise ValueError("first_name is required")
        if not isinstance(new_first_name, str):
            raise ValueError("first_name must be a string")
        self.__first_name = new_first_name

    @last_name.setter
    def last_name(self, new_last_name):
        if not new_last_name:
            raise ValueError("last_name is required")
        if not isinstance(new_last_name, str):
            raise ValueError("last_name must be a string")
        self.__last_name = new_last_name

    @email.setter
    def email(self, new_email):
        if not new_email:
            raise ValueError("email is required")
        if not isinstance(new_email, str):
            raise ValueError("email must be a string")
        self.__email = new_email

    def delete(self):
        # marks the guest as logically deleted
        if not self.__is_deleted:
            self.__is_deleted = True
            print(f"{self.__first_name} {self.__last_name} was marked as deleted.")
        else:
            print(f"{self.__first_name} {self.__last_name} is already marked as deleted.")

    @property
    def is_deleted(self):
        return self.__is_deleted

    def restore(self):
        # reverses the logical deletion of the guest
        if self.__is_deleted:
            self.__is_deleted = False
            print(f"{self.__first_name} {self.__last_name} was restored.")
        else:
            print(f"{self._first_name} {self.__last_name} is already active.")

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    @property
    def bookings(self):
        return self.__bookings

    def create_booking(self, room, check_in, check_out):
        # creates a new booking and adds it to the list of this guest
        new_booking = Booking(room, check_in, check_out)
        self.__bookings.append(new_booking)
        return new_booking
