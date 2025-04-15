from datetime import date

class Invoice:
    def __init__(self, invoice_id: int, booking_id: int, issue_date: date, total_amount: float, is_paid: bool = False):
        self.__invoice_id = invoice_id
        self.__booking_id = booking_id
        self.__issue_date = issue_date
        self.__total_amount = total_amount
        self.__is_paid = is_paid

    def get_invoice_id(self) -> int:
        return self.__invoice_id

    def get_issue_date(self) -> date:
        return self.__issue_date

    def set_issue_date(self, issue_date: date):
        self.__issue_date = issue_date

    def get_total_amount(self) -> float:
        return self.__total_amount

    def set_total_amount(self, amount: float):
        self.__total_amount = amount

    def mark_as_paid(self):
        self.__is_paid = True

    def is_invoice_paid(self) -> bool:
        return self.__is_paid

    def __repr__(self):
        return f"Invoice({self.__invoice_id}, total: {self.__total_amount}, paid: {self.__is_paid})"
