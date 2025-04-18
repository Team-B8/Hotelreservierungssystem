import model.ratings as model
import data_access.rating_dal as data_access

class RatingManager:
    def __init__(self) -> None:
        self.__rating_dal = data_access.RatingDAL()

    def create_rating(self, stars: int, comment: str, created_date: str) -> model.Rating:
        # Business-Logik: Sterne müssen zwischen 1 und 5 sein
        if not (1 <= stars <= 5):
            raise ValueError("Stars must be between 1 and 5")
        if not comment:
            raise ValueError("Comment cannot be empty")
        return self.__rating_dal.create_rating(stars, comment, created_date)

    def get_rating(self, rating_id: int) -> model.Rating | None:
        return self.__rating_dal.read_rating_by_id(rating_id)

    def delete_rating(self, rating_id: int) -> None:
        self.__rating_dal.delete_rating(rating_id)

