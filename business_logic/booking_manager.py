from datetime import date
from collections import defaultdict
from data_access.booking_dal import BookingDAL
from data_access.guest_dal import GuestDAL
from data_access.address_dal import AddressDAL
from model.guest import Guest
from model.booking import Booking
from model.address import Address
from business_logic.invoice_manager import InvoiceManager

class BookingManager:
    def __init__(self, invoice_manager=None):
        # invoice_manager is an entity of InvoiceManager for managing invoices.
        self.booking_dal = BookingDAL()
        self.guest_dal = GuestDAL()
        self.invoice_manager = invoice_manager if invoice_manager else InvoiceManager()

    def get_all_bookings(self):
        # return all bookings from the database
        return self.booking_dal.get_all_bookings()

    def create_booking_existing_guest(self, room_id: int, check_in, check_out, email: str, total_amount: float):
        guest = GuestDAL().get_by_email(email)
        if not guest:
            print("Guest not found.")
            return
        # create a Booking object for an existing guest
        booking = Booking(booking_id=None, room_id=room_id, guest_id=guest.guest_id, check_in=check_in, check_out=check_out, is_cancelled=False, total_amount=total_amount)
        # save the booking in the database
        booking = self.booking_dal.create_booking(booking)
        # return the created booking
        return booking
    
    def create_booking_new_guest(self, room_id: int, check_in, check_out, first_name: str, last_name: str, email: str, street: str, zip_code: str, city: str, total_amount: float):
        # Check if guest already exists
        guest = self.guest_dal.get_by_email(email)
        if guest:
            print("A guest with this email already exists. Using existing record.")
        # Create address
        address = Address(address_id=None, street=street, zip_code=zip_code, city=city)
        address_dal = AddressDAL()
        saved_address = address_dal.create(address)
        # Create new Guest
        new_guest = Guest(guest_id=None, first_name=first_name, last_name=last_name, email=email, address_id=saved_address.address_id)
        guest = self.guest_dal.create(new_guest)

        # Create booking
        booking = Booking(booking_id=None, room_id=room_id, guest_id=guest.guest_id, check_in=check_in, check_out=check_out, is_cancelled=False, total_amount=total_amount)
        booking = self.booking_dal.create_booking(booking)
        # return the created booking
        return booking

    def cancel_booking(self, booking_id: int) -> bool:
        # call the cancel_booking method from the data access layer
        success = self.booking_dal.cancel_booking(booking_id)
        if success:
            # call the cancel_booking method from the data access layer
            self.invoice_manager.mark_invoice_as_cancelled(booking_id)
        return success
    
    def get_booking_by_id(self, booking_id: int):
        # get a booking from the database by its ID
        return self.booking_dal.get_by_id(booking_id)

    def get_bookings_by_email(self, email: str):
        # find the guest by their email
        guest = self.guest_dal.get_by_email(email)
        # if guest exists, get all their bookings
        if guest:
            return self.booking_dal.get_by_guest_id(guest.guest_id)
        # if no guest found, return empty list
        return []
    
    def get_all_bookings_with_details(self):
        # call the get all bookings with details method from the data access layer
        return self.booking_dal.get_all_bookings_with_details()
    
    def get_room_type_occupancy_by_hotel(self, hotel_id: int):
        # returns the booking count for each room type for the given hotel
        return self.booking_dal.get_room_type_occupancy_by_hotel(hotel_id)
