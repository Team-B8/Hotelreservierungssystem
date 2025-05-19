from datetime import date
from model.room import Room
from model.invoice import Invoice

class Booking:
    def __init__(self, booking_id: int, guest_id: int, room_id: int, check_in: date, check_out: date, is_cancelled: bool, total_amount: float):
        if not booking_id:
            raise ValueError("booking_id is required")
        if not isinstance(booking_id, int):
            raise ValueError("booking_id must be an integer")
        if not guest_id:
            raise ValueError("guest_id is required")
        if not isinstance(guest_id, int):
            raise ValueError("guest_id must be an integer")
        if not room_id:
            raise ValueError("room_id is required")
        if not isinstance(room_id, int):
            raise ValueError("room_id must be an integer")
        if not check_in:
            raise ValueError("check_in is required")
        if not isinstance(check_in, date):
            raise TypeError("check_in must be a date object")
        if not check_out:
            raise ValueError("check_out is required")
        if not isinstance(check_out, date):
            raise TypeError("check_out must be a date object")
        if not isinstance(is_cancelled, bool):
            raise TypeError("is_cancelled must be a boolean")
        if not isinstance(total_amount, (int, float)):
            raise TypeError("total_amount must be a number")
        if total_amount < 0:
            raise ValueError("total_amount cannot be negative")

        self.__booking_id = booking_id
        self.__guest_id = guest_id
        self.__room_id = room_id
        self.__check_in = check_in
        self.__check_out = check_out
        self.__is_cancelled = is_cancelled
        self.__total_amount = float(total_amount)
        self.__invoice: Invoice | None = None
        self.__guest = None
        self.__room: Room | None = None

    def __repr__(self):
        return f"Booking({self.__booking_id}, RoomID={self.__room_id}, {self.__check_in} to {self.__check_out})"

    @property
    def booking_id(self) -> int:
        return self.__booking_id

    @property
    def guest_id(self) -> int:
        return self.__guest_id

    @property
    def room_id(self) -> int:
        return self.__room_id

    @property
    def check_in_date(self) -> date:
        return self.__check_in

    @check_in_date.setter
    def check_in_date(self, date_: date) -> None:
        if not isinstance(date_, date):
            raise TypeError("check_in_date must be a date object")
        self.__check_in = date_

    @property
    def check_out_date(self) -> date:
        return self.__check_out

    @check_out_date.setter
    def check_out_date(self, date_: date) -> None:
        if not isinstance(date_, date):
            raise TypeError("check_out_date must be a date object")
        self.__check_out = date_

    @property
    def total_amount(self) -> float:
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise TypeError("total_amount must be a number")
        if amount < 0:
            raise ValueError("total_amount cannot be negative")
        self.__total_amount = float(amount)

    @property
    def is_cancelled(self) -> bool:
        return self.__is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, is_cancelled: bool) -> None:
        if not isinstance(is_cancelled, bool):
            raise TypeError("is_cancelled must be a boolean")
        self.__is_cancelled = is_cancelled

    @property
    def room(self) -> Room | None:
        return self.__room

    @room.setter
    def room(self, room: Room) -> None:
        self.__room = room

    @property
    def invoice(self) -> Invoice | None:
        return self.__invoice

    @invoice.setter
    def invoice(self, invoice: Invoice) -> None:
        self.__invoice = invoice
