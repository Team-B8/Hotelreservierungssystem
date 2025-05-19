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

def user_story_1_2():
    print("\n--- 1.2: Hotels nach Sternen in Stadt filtern ---")
    city = input("Stadt eingeben: ")
    min_stars = int(input("Minimale Sterne (1–5): "))
    hotels = HotelManager().filter_by_city_and_stars(city, min_stars)
    for hotel in hotels:
        print(f"ID: {hotel.get_hotel_id()} | Name: {hotel.get_name()} | Sterne: {hotel.get_stars()}")

def user_story_1_3():
    print("\n--- 1.3: Hotels mit passenden Zimmern für Gästezahl in Stadt ---")
    city = input("Stadt: ")
    guests = int(input("Anzahl Gäste: "))
    hotels = HotelManager().filter_by_city_and_guest_capacity(city, guests)
    for hotel in hotels:
        print(f"Hotel: {hotel.get_name()} | Sterne: {hotel.get_stars()}")

def user_story_1_4():
    print("\n--- 1.4: Hotels mit verfügbaren Zimmern im Zeitraum ---")
    city = input("Stadt: ")
    check_in = input_date("Check-in Datum")
    check_out = input_date("Check-out Datum")
    hotels = HotelManager().filter_by_availability(city, check_in, check_out)
    for hotel in hotels:
        print(f"Hotel: {hotel.get_name()} | Sterne: {hotel.get_stars()}")
