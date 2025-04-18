# guest_manager.py (Business Logic Layer)
from data_access.guest_dal import GuestDAL
from model.guest import Guest

class GuestManager:
    def __init__(self):
        self.dal = GuestDAL()  # initializes the DAL layer

    def register_guest(self, first_name: str, last_name: str, email: str) -> Guest:
        # Creates a new guest if the email doesn't already exist
        guest = self.dal.get_by_email(email)
        if guest:
            print("A guest with this email already exists.")
            return guest
        new_guest = Guest(None, first_name, last_name, email)
        return self.dal.create(new_guest)

    def get_guest_by_id(self, guest_id: int) -> Guest | None:
        return self.dal.get_by_id(guest_id)

    def delete_guest(self, guest_id: int) -> bool:
        return self.dal.delete(guest_id)

    def restore_guest(self, guest_id: int) -> None:
        # Logically restores a previously deleted guest (not in DB)
        guest = self.dal.get_by_id(guest_id)
        if guest and guest.is_deleted:
            guest.restore()
            print(f"Guest {guest.full_name} was restored.")
