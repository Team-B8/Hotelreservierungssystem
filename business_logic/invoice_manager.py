from data_access.invoice_dal import InvoiceDAL
from data_access.room_dal import RoomDAL
from data_access.room_type_dal import RoomTypeDAL
from datetime import timedelta, date

class InvoiceManager:
    """Business logic for invoice creation, display, and adjustment."""
    def __init__(self):
        self.invoice_dal = InvoiceDAL()
        self.room_dal = RoomDAL()
        self.room_type_dal = RoomTypeDAL()

    def generate_invoice(self, booking):
        """Create an invoice for a given booking, calculating price with seasonal adjustments."""
        # Calculate the total price based on booking dates and room price
        room = self.room_dal.get_by_id(booking.room_id)
        room_type = self.room_type_dal.get_by_id(room.room_type_id)
        base_price = room_type.base_price
        total_amount = 0.0
        current_date = booking.start_date
        # Loop through each night from start_date to end_date (exclusive)
        while current_date < booking.end_date:
            # Determine season factor
            if current_date.month in [6, 7, 8]:
                factor = 1.5  # Summer high season
            elif current_date.month == 12:
                factor = 1.3  # Holiday season
            else:
                factor = 1.0  # Regular season
            total_amount += base_price * factor
            current_date += timedelta(days=1)
        # Round to 2 decimal places
        total_amount = round(total_amount, 2)
        from models.invoice import Invoice
        invoice = Invoice(booking_id=booking.id, amount=total_amount, paid=False)
        invoice = self.invoice_dal.create(invoice)
        return invoice

    def display_invoice(self, booking_id: int):
        """Retrieve an invoice by booking ID."""
        return self.invoice_dal.get_by_booking_id(booking_id)

    def adjust_invoice(self, booking_id: int, new_amount: float):
        """Adjust the amount of an invoice for a given booking ID."""
        invoice = self.invoice_dal.get_by_booking_id(booking_id)
        if invoice is None:
            return None
        invoice.amount = new_amount
        self.invoice_dal.update(invoice)
        return invoice