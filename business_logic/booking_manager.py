from data_access.booking_dal import BookingDAL
from data_access.guest_dal import GuestDAL

class BookingManager:
    """Business logic for creating and cancelling bookings."""
    def __init__(self, invoice_manager):
        # invoice_manager is an instance of InvoiceManager for handling invoices
        self.booking_dal = BookingDAL()
        self.guest_dal = GuestDAL()
        self.invoice_manager = invoice_manager

    def create_booking(self, room_id: int, first_name: str, last_name: str, email: str, start_date, end_date):
        """Create a booking for the given room and guest information, and generate an invoice."""
        # Ensure guest exists or create new guest
        guest = self.guest_dal.get_by_email(email)
        if guest is None:
            # Create a new Guest record
            from models.guest import Guest
            guest = Guest(first_name=first_name, last_name=last_name, email=email)
            guest = self.guest_dal.create(guest)
        # Create booking record
        from models.booking import Booking
        booking = Booking(room_id=room_id, guest_id=guest.id, start_date=start_date, end_date=end_date, status=False)
        booking = self.booking_dal.create(booking)
        # Generate invoice for the booking
        self.invoice_manager.generate_invoice(booking)
        return booking

    def cancel_booking(self, booking_id: int) -> bool:
        """Cancel an existing booking by its ID."""
        return self.booking_dal.cancel_booking(booking_id)

    def get_bookings_for_guest(self, email: str):
        """Retrieve active bookings for a guest by email."""
        guest = self.guest_dal.get_by_email(email)
        if guest is None:
            return []
        return self.booking_dal.get_by_guest_id(guest.id, active_only=True)