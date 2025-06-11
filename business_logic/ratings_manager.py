from data_access.rating_dal import RatingDAL
from data_access.booking_dal import BookingDAL
from data_access.room_dal import RoomDAL
from data_access.guest_dal import GuestDAL
from data_access.hotel_dal import HotelDAL
from model.ratings import Rating
from model.room import Room
from model.hotel import Hotel
from model.guest import Guest
from datetime import date


class RatingManager:
    def __init__(self) -> None:
        # initialise all required DALs
        self.__rating_dal = RatingDAL()
        self.__booking_dal = BookingDAL()
        self.__room_dal = RoomDAL()
        self.__hotel_dal = HotelDAL()
        self.__guest_dal = GuestDAL()

    def create_rating(self, stars: int, comment: str, created_date: date, hotel_id: int, guest_id: int) -> Rating:
        # Business-Logic: Stars must be between 1 and 5
        if not (1 <= stars <= 5):
            raise ValueError("Sterne müssen zwischen 1 und 5 liegen")
        if not comment:
            raise ValueError("Kommentar darf nicht leer sein")
        # Create a Rating objekt an pass it to the DAL dor database insertion
        rating = Rating(rating_id=None, stars=stars, comment=comment, created_date=created_date, hotel_id=hotel_id, guest_id=guest_id)
        return self.__rating_dal.create(rating)
     

    def get_ratings_by_hotel_id(self, hotel_id: int) -> list[Rating]:
        # Retrieve all ratings for a given hotel ID
        return self.__rating_dal.read_by_hotel_id(hotel_id)

    def has_completed_booking(self, check_out_date: date) -> bool:
        # Check if a booking has been completed based on check-out date
        return self.__booking_dal.has_completed_booking(check_out_date)
    
    def get_room_by_id(self, room_id: int) -> Room:
        # Return a Room object based on its ID
        return self.__room_dal.get_by_id(room_id)

    def get_hotel_by_id(self, hotel_id: int) -> Hotel:
        # Return a Hotel object based on its ID
        return self.__hotel_dal.read_hotel_by_id(hotel_id)

    def get_completed_bookings_by_guest_id(self, guest_id: int) -> list:
        # Return a list of completed bookings for a specific guest
        return self.__booking_dal.get_completed_bookings_by_guest_id(guest_id)

    def get_guest_id_by_email(self, email: str) -> int:
        # Lookup a guest by email and return their ID, or raise an error if not found
        guest = self.__guest_dal.get_by_email(email)
        if guest is None:
            raise ValueError("No guest found with this email.")
        return guest.guest_id
