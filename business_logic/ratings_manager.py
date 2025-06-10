from data_access.rating_dal import RatingDAL
from data_access.booking_dal import BookingDAL
from data_access.room_dal import RoomDAL
from data_access.guest_dal import GuestDAL
from data_access.hotel_dal import HotelDAL
from model.ratings import Rating
from model.room import Room
from model.hotel import Hotel
from datetime import date


class RatingManager:
    def __init__(self) -> None:
        self.__rating_dal = RatingDAL()
        self.__booking_dal = BookingDAL()
        self.__room_dal = RoomDAL()
        self.__hotel_dal = HotelDAL()
    


    def create_rating(self, stars: int, comment: str, created_date: str, hotel_id: int, guest_id: int) -> Rating:
        # Business-Logic: Stars must be between 1 and 5
        if not (1 <= stars <= 5):
            raise ValueError("Stars must be between 1 and 5")
        if not comment:
            raise ValueError("Comment cannot be empty")
        rating = Rating(None, stars, comment, created_date, hotel_id, guest_id)
        return self.__rating_dal.create(rating)

    def get_ratings_by_hotel_id(self, hotel_id: int) -> list[Rating]:
        return self.__rating_dal.read_by_hotel_id(hotel_id)

    def has_completed_booking(self, check_out_date: date) -> bool:
        return self.__booking_dal.has_completed_booking(check_out_date)
    
    def get_room_by_id(self, room_id: int) -> Room:
        return self.__room_dal.get_by_id(room_id)

    def get_hotel_by_id(self, hotel_id: int) -> Hotel:
        return self.__hotel_dal.read_hotel_by_id(hotel_id)

    def get_completed_bookings_by_guest_id(self, guest_id: int) -> list:
        return self.__booking_dal.get_completed_bookings_by_guest_id(guest_id)

    #def get_rating(self, rating_id: int) -> model.Rating | None:
        return self.__rating_dal.read_rating_by_id(rating_id)
    #get_rating(rating_id) would be useful, for example, if an admin wants to check or change a specific rating or wants to look up a specific rating from an ID
    #def delete_rating(self, rating_id: int) -> None:
        self.__rating_dal.delete_rating(rating_id)

