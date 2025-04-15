from data_access.booking_dal import BookingDAL
from data_access.invoice_dal import InvoiceDAL
from model.booking import Booking
from model.invoice import Invoice
from model.room import Room
from datetime import date

class BookingManager:
    def __init__(self):
        # Initialize data access layers for bookings and invoices
        self.__booking_dal = BookingDAL()
        self.__invoice_dal = InvoiceDAL()

    def create_booking(self, guest_id: int, room: Room, check_in: date, check_out: date, price: float) -> Booking:
        # Save the booking to the database
        booking = self.__booking_dal.create_booking(guest_id, room, check_in, check_out, price)
        # Automatically create an invoice for the booking
        invoice = self.__invoice_dal.create_invoice(booking.booking_id, date.today(), price)
        # Link the invoice to the booking
        booking.set_invoice(invoice)
        return booking

    def cancel_booking(self, booking_id: int) -> None:
        # Cancel the booking with the given ID
        self.__booking_dal.cancel_booking(booking_id)

    def get_booking(self, booking_id: int) -> Booking | None:
        # Retrieve a booking by its ID
        return self.__booking_dal.get_booking_by_id(booking_id)
