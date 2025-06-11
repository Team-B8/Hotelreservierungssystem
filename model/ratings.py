from datetime import date

class Rating:
    def __init__(self, rating_id: int | None, stars: int, comment: str, created_date: date, hotel_id: int, guest_id: int):
        if rating_id is not None and not isinstance(rating_id, int):
            raise TypeError("rating_id muss eine Ganzzahl oder kein Wert sein")
        if not isinstance(stars, int) or not (1 <= stars <= 5):
            raise ValueError("Die Sterne müssen eine ganze Zahl zwischen 1 und 5 sein.")
        if not comment:
            raise ValueError("Kommentar ist erforderlich")
        if not isinstance(comment, str):
            raise TypeError("Kommentar muss eine Zeichenkette sein")
        if not isinstance(hotel_id, int):
            raise TypeError("hotel_id muss eine ganze Zahl sein")
        if not isinstance(guest_id, int):
            raise TypeError("guest_id muss eine ganze Zahl sein")        
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
        # Allows setting the ID after inserting into the database 
        if not isinstance(value, int) and value is not None:
            raise ValueError("rating_id muss eine ganze Zahl sein")
        self.__rating_id = value
        
    @property
    def stars(self) -> int:
        return self.__stars

    @stars.setter
    def stars(self, value: int):
        # Ensures star value is always between 1 and 5
        if not isinstance(value, int) or not (1 <= value <= 5):
            raise ValueError("Sterne müssen eine ganze Zahl zwischen 1 und 5 sein.")
        self.__stars = value

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, value: str):
        # Allows updating comment while ensuring correct type
        if not isinstance(value, str) and value is not None:
            raise TypeError("Kommentar muss ein String oder None sein")
        self.__comment = value

    @property
    def created_date(self) -> date:
        # Read-only access to the date the rating was created
        return self.__created_date    
