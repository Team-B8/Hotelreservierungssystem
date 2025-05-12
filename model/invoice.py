from datetime import date

class Invoice:
    def __init__(self, invoice_id: int, booking_id: int, issue_date: date, total_amount: float, is_paid: bool = False):
        
        if invoice_id < 0:
            raise ValueError("invoice_id must be positive")
        if not invoice_id:
            raise ValueError("invoice_id is required")
        if not booking_id:
            raise ValueError("booking_id is required")
        if not issue_date:
            raise ValueError("issue_date is required")
        if not total_amount:
            raise ValueError("total_amound is required")
        if not is_paid:
            raise ValueError("is_paid is required")
        
        self.__invoice_id = invoice_id
        self.__booking_id = booking_id
        self.__issue_date = issue_date
        self.__total_amount = total_amount
        self.__is_paid = is_paid

    def __repr__(self):
        return f"Invoice({self.__invoice_id}, total: {self.__total_amount}, paid: {self.__is_paid})"

    def get_invoice_id(self) -> int:
        return self.__invoice_id

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
    def is_paid(self) -> bool:
        return self.__is_paid

    @is_paid.setter
    def is_paid(self):
        self.__is_paid = True
    
    @property
    def booking(self) -> int:
        return self.__booking_id
    
    @booking.setter
    def booking(self, booking: int):
        self.__booking_id = booking

