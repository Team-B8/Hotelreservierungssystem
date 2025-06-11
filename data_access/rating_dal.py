from data_access.base_dal import BaseDAL
from model.ratings import Rating

class RatingDAL(BaseDAL):
    def __init__(self):
    # Call the constructor of the base class (BaseDAL)
    # This sets up the database connection
        super().__init__()

    def create(self, rating: Rating) -> Rating:
        # Inserts a new rating into the database
        sql = "INSERT INTO Rating (stars, comment, hotel_id, created_date, guest_id) VALUES (?, ?, ?, ?, ?)"
        # Collect values from the Rating object
        params = (rating.stars, rating.comment, rating.created_date, rating.hotel_id, rating.guest_id)
        # Open a database connection using the inherited method _connect()
        with self._connect() as conn:
            # Execute the SQL statement with the given parameters
            cursor = conn.execute(sql, params)
            # Save the changes to the database
            conn.commit()
            # Get the ID of the newly inserted row and set it on the object
            rating.rating_id = cursor.lastrowid
        return rating

    def read_by_hotel_id(self, hotel_id: int) -> list[Rating]:
        # Select all ratings for a given hotel ID
        sql = "SELECT rating_id, stars, comment, created_date, guest_id, hotel_id FROM Rating WHERE hotel_id = ?"
        with self._connect() as conn:
            cursor = conn.execute(sql, (hotel_id,))
            rows = cursor.fetchall()
        return [Rating(*row) for row in rows]
