from data_access.guest_dal import GuestDAL
from model.guest import Guest

class GuestManager:
    def __init__(self):
        self.dal = GuestDAL()  # initializes the DAL layer

    def register_guest(self, first_name: str, last_name: str, email: str) -> Guest:
        # Creates a new guest if the email doesn't already exist
        guest = self.dal.get_by_email(email)
        if guest:
            print("Ein Gast mit dieser E-Mail existiert bereits.")
            return guest
        new_guest = Guest(None, first_name, last_name, email)
        return self.dal.create(new_guest)

    def get_guest_by_id(self, guest_id: int) -> Guest | None:
        return self.dal.get_by_id(guest_id)
