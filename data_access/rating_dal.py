from data_access.base_dal import BaseDAL
from model.ratings import Rating

class RatingDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def create_rating(self, stars: int, comment: str, created_date: str) -> Rating:
        sql = "INSERT INTO Rating (Stars, Comment, CreatedDate) VALUES (?, ?, ?)"
        params = (stars, comment, created_date)
        with self._connect() as conn:
            cursor = conn.execute(sql, params)
            conn.commit()
            last_row_id = cursor.lastrowid
        return Rating(last_row_id, stars, comment, created_date)

    def read_rating_by_id(self, rating_id: int) -> Rating | None:
        sql = "SELECT RatingId, Stars, Comment, CreatedDate FROM Rating WHERE RatingId = ?"
        params = (rating_id,)
        with self._connect() as conn:
            cursor = conn.execute(sql, params)
            result = cursor.fetchone()
        if result:
            rating_id, stars, comment, created_date = result
            return Rating(rating_id, stars, comment, created_date)
        return None

    def delete_rating(self, rating_id: int) -> None:
        sql = "DELETE FROM Rating WHERE RatingId = ?"
        params = (rating_id,)
        with self._connect() as conn:
            conn.execute(sql, params)
            conn.commit()
