from data_access.invoice_dal import InvoiceDAL
from data_access.room_dal import RoomDAL
from data_access.room_type_dal import RoomTypeDAL
from data_access.guest_dal import GuestDAL
from data_access.booking_dal import BookingDAL
from model.invoice import Invoice
from datetime import timedelta, date

class InvoiceManager:
    def __init__(self):
        self.invoice_dal = InvoiceDAL()
        self.room_dal = RoomDAL()
        self.room_type_dal = RoomTypeDAL()

    def generate_invoice(self, booking):
        room = self.room_dal.get_by_id(booking.room_id)
        room_type = self.room_type_dal.get_by_id(room.type_id)

        # Determine base price
        base_price = room.price_per_night
        total_amount = 0.0
        current_date = booking.check_in_date

        # Loop through each night of the stay
        while current_date < booking.check_out_date:
            if current_date.month in [6, 7, 8]:        # Summer high season
                factor = 1.5
            elif current_date.month == 12:             # Winter holiday season
                factor = 1.3
            else:
                factor = 1.0                            # Normal season

            total_amount += base_price * factor
            current_date += timedelta(days=1)

        total_amount = round(total_amount, 2)

        # Create invoice
        invoice = Invoice(booking_id=booking.booking_id, issue_date=date.today(), total_amount=total_amount, is_paid=False)

        return self.invoice_dal.create(invoice)
    
    def display_invoice(self, booking_id: int) -> Invoice | None:
        return self.invoice_dal.get_by_booking_id(booking_id)

    def adjust_invoice(self, booking_id: int, new_amount: float) -> Invoice | None:
        invoice = self.invoice_dal.get_by_booking_id(booking_id)
        if invoice is None:
            return None
        invoice.total_amount = new_amount
        self.invoice_dal.update(invoice)
        return invoice

    def get_invoices_by_email(self, email: str):
        # get the guest object by email
        guest = GuestDAL().get_by_email(email)
        # if guest not found, return empty list
        if not guest:
            return []
        # get all bookings for the guest
        booking_dal = BookingDAL()
        bookings = booking_dal.get_by_guest_email(guest.email)
        invoices = []
        # for each booking, try to get the invoice
        for booking in bookings:
            invoice = self.invoice_dal.get_by_booking_id(booking.booking_id)
            if invoice:
                invoices.append(invoice)
        # return list of found invoices
        return invoices
    
    def get_invoice_by_booking_id(self, booking_id: int) -> Invoice | None:
        return self.invoice_dal.get_by_booking_id(booking_id)