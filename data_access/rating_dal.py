from data_access.base_dal import BaseDAL
from model.ratings import Rating

class RatingDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def create(self, rating: Rating) -> Rating:
        # Inserts a new rating into the database
        sql = "INSERT INTO Rating (stars, comment, hotel_id, created_date, guest_id) VALUES (?, ?, ?, ?, ?)"
        params = (rating.stars, rating.comment, rating.created_date, rating.hotel_id, rating.guest_id)
        with self._connect() as conn:
            cursor = conn.execute(sql, params)
            conn.commit()
            rating.rating_id = cursor.lastrowid
        return rating

    def read_by_hotel_id(self, hotel_id: int) -> list[Rating]:
        sql = "SELECT rating_id, stars, comment, created_date, guest_id, hotel_id FROM Rating WHERE hotel_id = ?"
        with self._connect() as conn:
            cursor = conn.execute(sql, (hotel_id,))
            rows = cursor.fetchall()
        return [Rating(*row) for row in rows]
