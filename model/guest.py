# Guest
class Guest:
    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str):
        self._guest_id = guest_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._bookings = []  # list to store associated bookings
        self._is_deleted = False  # flag to mark logical deletion

    @property
    def guest_id(self):
        return self._guest_id

    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name):
        # update first name only if it is different
        if new_first_name != self._first_name:
            self._first_name = new_first_name
        else:
            print(f"The new first name is the same as the first name before.")

    @last_name.setter
    def last_name(self, new_last_name):
        # update last name only if it is different
        if new_last_name != self._last_name:
            self._last_name = new_last_name
        else:
            print(f"The new last name is the same as the last name before.")

    @email.setter
    def email(self, new_email):
        # update email only if it is different
        if self.email != new_email:
            self._email = new_email
        else:
            print(f"The new email is the same as before.")

    def delete(self):
        # marks the guest as logically deleted
        if not self._is_deleted:
            self._is_deleted = True
            print(f"{self._first_name} {self._last_name} was marked as deleted.")
        else:
            print(f"{self._first_name} {self._last_name} is already marked as deleted.")

    @property
    def is_deleted(self):
        return self._is_deleted

    def restore(self):
        # reverses the logical deletion of the guest
        if self._is_deleted:
            self._is_deleted = False
            print(f"{self._first_name} {self._last_name} was restored.")
        else:
            print(f"{self._first_name} {self._last_name} is already active.")

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def bookings(self):
        return self._bookings

    def create_booking(self, room, check_in, check_out):
        # creates a new booking and adds it to the list of this guest
        new_booking = Booking(room, check_in, check_out)
        self._bookings.append(new_booking)
        return new_booking
