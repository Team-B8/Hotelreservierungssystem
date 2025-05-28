from data_access.booking_dal import BookingDAL
from data_access.guest_dal import GuestDAL
from model.guest import Guest
from model.booking import Booking

class BookingManager:
    def __init__(self, invoice_manager):
        # invoice_manager is an instance of InvoiceManager for handling invoices
        self.booking_dal = BookingDAL()
        self.guest_dal = GuestDAL()
        self.invoice_manager = invoice_manager

    def create_booking(self, room_id: int, start_date, end_date, first_name: str, last_name: str, email: str):
        # Ensure guest exists or create new guest
        guest = self.guest_dal.get_by_email(email)
        if guest is None:
            # Create a new Guest record
            guest = Guest(first_name=first_name, last_name=last_name, email=email)
            guest = self.guest_dal.create(guest)
        # Create booking record
        booking = Booking(room_id=room_id, guest_id=guest.id, start_date=start_date, end_date=end_date, status=False)
        booking = self.booking_dal.create(booking)
        # Generate invoice for the booking
        self.invoice_manager.generate_invoice(booking)
        return booking

    def cancel_booking(self, booking_id: int) -> bool:
        return self.booking_dal.cancel_booking(booking_id)

    def get_bookings_for_guest(self, email: str):
        guest = self.guest_dal.get_by_email(email)
        if guest is None:
            return []
        return self.booking_dal.get_by_guest_id(guest.id, active_only=True)