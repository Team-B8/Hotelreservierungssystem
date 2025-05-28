from datetime import date

class Invoice:
    def __init__(self, booking_id: int, issue_date: date, total_amount: float, invoice_id: int | None=None):

        if not booking_id:
            raise ValueError("booking_id is required")
        if not issue_date:
            raise ValueError("issue_date is required")
        if not total_amount:
            raise ValueError("total_amount is required")
        
        self.__invoice_id = invoice_id
        self.__booking_id = booking_id
        self.__issue_date = issue_date
        self.__total_amount = total_amount

    def __repr__(self):
        return f"Invoice({self.__invoice_id}, total: {self.__total_amount})"

    @property
    def invoice_id(self) -> int:
        return self.__invoice_id
    
    @invoice_id.setter
    def invoice_id(self, value: int):
        self.__invoice_id = value

    @property
    def issue_date(self) -> date:
        return self.__issue_date

    @issue_date.setter
    def issue_date(self, issue_date: date):
        self.__issue_date = issue_date

    @property
    def total_amount(self) -> float:
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, amount: float):
        self.__total_amount = amount
    
    @property
    def booking_id(self) -> int:
        return self.__booking_id
    
    @booking_id.setter
    def booking_id(self, booking: int):
        self.__booking_id = booking

