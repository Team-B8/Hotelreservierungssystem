class Rating:
    def __init__(self, rating_id: int, stars: int, comment: str, created_date: str):
        self.__rating_id = rating_id
        self.__stars = stars
        self.__comment = comment
        self.__created_date = created_date

    @property
    def rating_id(self) -> int:
        return self.__rating_id

    @property
    def stars(self) -> int:
        return self.__stars

    def set_stars(self, stars: int) -> None:
        self.__stars = stars
    @property
    def comment(self) -> str:
        return self.__comment

    def set_comment(self, comment: str) -> None:
        self.__comment = comment

    @property
    def created_date(self) -> str:
        return self.__created_date

    def delete(self) -> None:
        del self
