from business_logic.hotel_manager import HotelManager
from datetime import datetime

def input_date(prompt):
    while True:
        try:
            return datetime.strptime(input(prompt + ' (YYYY-MM-DD): '), "%Y-%m-%d").date()
        except ValueError:
            print("Ungültiges Datum. Bitte erneut eingeben.")

def user_story_1_1():
    print("\n--- 1.1: Hotels nach Stadt filtern ---")
    city = input("Stadt eingeben: ")
    hotels = HotelManager().filter_by_city(city)
    for hotel in hotels:
        print(f"ID: {hotel.get_hotel_id()} | Name: {hotel.get_name()} | Sterne: {hotel.get_stars()}")
