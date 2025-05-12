from datetime import date
from model import Room
from model import Invoice

class Booking:
    def __init__(self, booking_id: int, guest_id: int, room_id: int, check_in: date, check_out: date, is_cancelled: bool, total_amount: float):
        
        if not guest_id:
            raise ValueError("guest_id is required")
        if not room_id:
            raise ValueError("room_id is required")
        if not check_in:
            raise ValueError("check_in is required")
        if not check_out:
            raise ValueError("check_out is required")
        if not isinstance(is_cancelled, bool):
            raise TypeError("is_cancelled must be a boolean")
        if total_amount < 0:
            raise ValueError("total_amount cannot be negative")
        
        self.__booking_id = booking_id
        self.__guest_id = guest_id
        self.__room = room_id
        self.__check_in = check_in
        self.__check_out = check_out
        self.__is_cancelled = is_cancelled
        self.__total_amount = total_amount
        self.__invoice = None
        self.__guest = None
        self.__room = None

    def __repr__(self):
        return f"Booking({self.__booking_id}, Room={self.__room}, {self.__check_in} to {self.__check_out})"

    def get_booking_id(self) -> int:
        return self.__booking_id

    @property
    def check_in_date(self) -> date:
        return self.__check_in

    @property
    def check_out_date(self) -> date:
        return self.__check_out

    @check_in_date.setter
    def check_in_date(self, date_: date):
        self.__check_in = date_

    @check_out_date.setter
    def check_out_date(self, date_: date):
        self.__check_out = date_

    @property
    def total_amount(self) -> float:
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, amount: float):
        self.__total_amount = amount

    @property
    def is_cancelled(self):
        self.__is_cancelled = True
    
    @is_cancelled.setter
    def is_cancelled(self, is_cancelled: bool):
        if not isinstance(is_cancelled, bool):
            raise TypeError("is_cancelled must be a boolean")
        self.__is_cancelled = is_cancelled        

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, room: Room):
        self.__room = room

    @property
    def invoice(self) -> Invoice:
        return self.__invoice

    @invoice.setter
    def invoice(self, invoice: Invoice):
        self.__invoice = invoice
