from data_access.base_dal import BaseDAL
from model.ratings import Rating

class RatingDAL(BaseDAL):
    def create_rating(self, stars: int, comment: str, created_date: str) -> model.Rating:
        sql = "
        INSERT INTO Rating (Stars, Comment, CreatedDate) VALUES (?, ?, ?)
        "
        params = (stars, comment, created_date)
        last_row_id, _ = self.execute(sql, params)
        return model.Rating(last_row_id, stars, comment, created_date)

    def read_rating_by_id(self, rating_id: int) -> model.Rating | None:
        sql = "
        SELECT RatingId, Stars, Comment, CreatedDate FROM Rating WHERE RatingId = ?
        "
        params = (rating_id,)
        result = self.fetchone(sql, params)
        if result:
            rating_id, stars, comment, created_date = result
            return model.Rating(rating_id, stars, comment, created_date)
        return None

    def delete_rating(self, rating_id: int) -> None:
        sql = "DELETE FROM Rating WHERE RatingId = ?"
        params = (rating_id,)
        self.execute(sql, params)
