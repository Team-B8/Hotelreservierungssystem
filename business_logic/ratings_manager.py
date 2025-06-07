from data_access.rating_dal import RatingDAL
from data_access.booking_dal import BookingDAL
from model.ratings import Rating

class RatingManager:
    def __init__(self) -> None:
        self.__rating_dal = RatingDAL()
        self.__booking_dal = BookingDAL()


    def create_rating(self, stars: int, comment: str, created_date: str, hotel_id: int, guest_id: int) -> Rating:
        # Business-Logik: Sterne müssen zwischen 1 und 5 sein
        if not (1 <= stars <= 5):
            raise ValueError("Stars must be between 1 and 5")
        if not comment:
            raise ValueError("Comment cannot be empty")
        if not self.__booking_dal.has_completed_booking(guest_id, hotel_id):
            raise PermissionError("Guest can only rate after a completed, non cancelled stay.")
        rating = Rating(stars, comment, created_date, hotel_id, guest_id)
        return self.__rating_dal.create(rating)
    

    #def get_rating(self, rating_id: int) -> model.Rating | None:
        return self.__rating_dal.read_rating_by_id(rating_id)

    #def delete_rating(self, rating_id: int) -> None:
        self.__rating_dal.delete_rating(rating_id)

