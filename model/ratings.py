class Rating:
    def __init__(self, rating_id: int, stars: int, comment: str, created_date: str):
        self.__rating_id = rating_id
        self.__stars = stars
        self.__comment = comment
        self.__created_date = created_date

    def get_rating_id(self) -> int:
        return self.__rating_id

    def get_stars(self) -> int:
        return self.__stars

    def set_stars(self, stars: int) -> None:
        self.__stars = stars

    def get_comment(self) -> str:
        return self.__comment

    def set_comment(self, comment: str) -> None:
        self.__comment = comment

    def get_created_date(self) -> str:
        return self.__created_date

    def delete(self) -> None:
        del self

