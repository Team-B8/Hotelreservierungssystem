from datetime import date
from model.room import Room
from model.invoice import Invoice

class Booking:
    def __init__(self, booking_id: int, guest_id: int, room: Room, check_in: date, check_out: date, is_cancelled: bool, total_amount: float):
        self.__booking_id = booking_id
        self.__guest_id = guest_id
        self.__room = room
        self.__check_in = check_in
        self.__check_out = check_out
        self.__is_cancelled = is_cancelled
        self.__total_amount = total_amount
        self.__invoice = None  # Typ: Invoice | None

    def get_booking_id(self) -> int:
        return self.__booking_id

    def get_check_in_date(self) -> date:
        return self.__check_in

    def get_check_out_date(self) -> date:
        return self.__check_out

    def set_check_in_date(self, date_: date):
        self.__check_in = date_

    def set_check_out_date(self, date_: date):
        self.__check_out = date_

    def get_total_amount(self) -> float:
        return self.__total_amount

    def set_total_amount(self, amount: float):
        self.__total_amount = amount

    def cancel(self):
        self.__is_cancelled = True

    def set_room(self, room: Room):
        self.__room = room

    def get_invoice(self) -> Invoice:
        return self.__invoice

    def set_invoice(self, invoice: Invoice):
        self.__invoice = invoice

    def __repr__(self):
        return f"Booking({self.__booking_id}, Room={self.__room}, {self.__check_in} to {self.__check_out})"
