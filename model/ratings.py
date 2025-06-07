from datetime import date

class Rating:
    def __init__(self, rating_id: int | None, stars: int, comment: str, created_date: date, hotel_id: int, guest_id: int):
        if rating_id is not None and not isinstance(rating_id, int):
            raise TypeError("rating_id must be an integer or None")
        if not isinstance(stars, int) or not (1 <= stars <= 5):
            raise ValueError("Stars must be an integer between 1 and 5.")
        if not comment:
            raise ValueError("comment is required")
        if not isinstance(comment, str):
            raise TypeError("comment must be a string")
        if not isinstance(hotel_id, int):
            raise TypeError("hotel_id must be an integer")
        if not isinstance(guest_id, int):
            raise TypeError("guest_id must be an integer")        
        self.__rating_id = rating_id
        self.__stars = stars
        self.__comment = comment
        self.__created_date = created_date
        self.hotel_id = hotel_id
        self.guest_id = guest_id
    


    def __repr__(self):
        return f"Rating(id={self.__rating_id}, stars={self.__stars}, comment{self.__comment}, created_date{self.__created_date}, hotel_id{self.hotel_id}. guest_id{self.guest_id})"

    @property
    def rating_id(self) -> int:
        return self.__rating_id
    
    @rating_id.setter
    def rating_id(self, value: int):
        if not isinstance(value, int) and value is not None:
            raise ValueError("rating_id must be an Integer")
        self.__rating_id = value
        

    @property
    def stars(self) -> int:
        return self.__stars

    @stars.setter
    def stars(self, value: int):
        if not isinstance(value, int) or not (1 <= value <= 5):
            raise ValueError("Stars musst be an Integer between 1 and 5.")
        self.__stars = value

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, value: str):
        if not isinstance(value, str) and value is not None:
            raise TypeError("comment must be a string or None")
        self.__comment = value

    @property
    def created_date(self) -> date:
        return self.__created_date    
