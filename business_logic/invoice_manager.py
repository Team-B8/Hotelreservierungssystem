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

    def _get_season_factor(self, current_date):
        # return a price factor based on the month (season)
        if current_date.month in [6, 7, 8]:        # Summer high season
            return 1.5
        elif current_date.month == 12:             # Winter holiday season
            return 1.3
        else:
            return 1.0                             # normal season

    def calculate_dynamic_price(self, base_price: float, check_in: date, check_out: date) -> float:
        total = 0.0
        current_date = check_in
        # loop through each day of the stay
        while current_date < check_out:
            # get seasonal factor
            factor = self._get_season_factor(current_date)
            # add adjusted price for the day
            total += base_price * factor
            # go to next day
            current_date += timedelta(days=1)
        # return the total price for the stay
        return total

    def generate_invoice(self, booking):
        room = self.room_dal.get_by_id(booking.room_id)
        room_type = self.room_type_dal.get_by_id(room.type_id)
        # Determine base price
        base_price = room.price_per_night
        total_amount = self.calculate_dynamic_price(booking.check_in, booking.check_out, base_price)
        # Create invoice
        invoice = Invoice(booking_id=booking.booking_id, issue_date=date.today(), total_amount=total_amount, is_cancelled=False)
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
    
    def mark_invoice_as_cancelled(self, booking_id: int) -> bool:
        # mark invoice as cancelled
        return self.invoice_dal.mark_invoice_as_cancelled(booking_id)
    
    def get_total_revenue(self, start_date: date, end_date: date, hotel_id: int| None = None) -> float:
        # Retrieve all invoices from the database
        invoices = self.invoice_dal.get_all_by_date_and_hotel(start_date, end_date, hotel_id)
        total = 0.0
        # Loop through each invoice
        for invoice in invoices:
            if invoice.is_cancelled or not (start_date <= invoice.issue_date <= end_date):
                continue
            if hotel_id:
                booking = BookingDAL().get_by_id(invoice.booking_id)
                room = self.room_dal.get_by_id(booking.room_id)
                if room.hotel_id != hotel_id:
                    continue
            total += invoice.total_amount
        # Return the total revenue for the period
        return total
    
    def get_monthly_revenue_range(self, start_date: date, end_date: date, hotel_id: int | None = None) -> dict[str, float]:
        invoices = self.invoice_dal.get_all_by_date_and_hotel(start_date, end_date, hotel_id)
        revenue = {}
        for invoice in invoices:
            if invoice.is_cancelled or not (start_date <= invoice.issue_date <= end_date):
                continue
            if hotel_id:
                booking = BookingDAL().get_by_id(invoice.booking_id)
                room = self.room_dal.get_by_id(booking.room_id)
                if room.hotel_id != hotel_id:
                    continue
            month_key = invoice.issue_date.strftime("%Y-%m-01")
            revenue[month_key] = revenue.get(month_key, 0.0) + invoice.total_amount
        return revenue