import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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
        print(f"ID: {hotel.hotel_id} | Name: {hotel.name} | Sterne: {hotel.stars}")

def user_story_1_2():
    print("\n--- 1.2: Hotels nach Sternen in Stadt filtern ---")
    city = input("Stadt eingeben: ")
    min_stars = int(input("Minimale Sterne (1–5): "))
    hotels = HotelManager().filter_by_city_and_stars(city, min_stars)
    for hotel in hotels:
        print(f"ID: {hotel.hotel_id} | Name: {hotel.name} | Sterne: {hotel.stars}")

def user_story_1_3():
    print("\n--- 1.3: Hotels mit passenden Zimmern für Gästezahl in Stadt ---")
    city = input("Stadt: ")
    guests = int(input("Anzahl Gäste: "))
    hotels = HotelManager().filter_by_city_and_guest_capacity(city, guests)
    for hotel in hotels:
        print(f"Hotel: {hotel.name} | Sterne: {hotel.stars}")

def user_story_1_4():
    print("\n--- 1.4: Hotels mit verfügbaren Zimmern im Zeitraum ---")
    city = input("Stadt: ")
    check_in = input_date("Check-in Datum")
    check_out = input_date("Check-out Datum")
    hotels = HotelManager().filter_by_availability(city, check_in, check_out)
    for hotel in hotels:
        print(f"Hotel: {hotel.name} | Sterne: {hotel.stars}")

def user_story_1_5():
    print("\n--- 1.5: Kombinierte Suche (Stadt, Gästezahl, Sterne, Zeitraum) ---")
    city = input("Stadt: ")
    guests = int(input("Anzahl Gäste: "))
    stars = int(input("Minimale Sterne: "))
    check_in = input_date("Check-in Datum")
    check_out = input_date("Check-out Datum")
    hotels = HotelManager().filter_combined(city, guests, stars, check_in, check_out)
    for hotel in hotels:
        print(f"Hotel: {hotel.name} | Sterne: {hotel.stars}")


def user_story_1_6():
    print("\n--- 1.6: Hotelinformationen anzeigen ---")
    hotels = HotelManager().get_all_hotels()
    for hotel in hotels:
        address = hotel.get_address()
        print(f"{hotel.name} | {hotel.stars} Sterne | Adresse: {address.get_full_address()}")

def gast_menu():
    while True:
        print("\n--- GAST MENÜ ---")
        print("1.1 Hotels nach Stadt filtern")
        print("1.2 Hotels nach Sternen in Stadt filtern")
        print("1.3 Hotels mit passenden Zimmern für Gästezahl")
        print("1.4 Hotels mit verfügbaren Zimmern im Zeitraum")
        print("1.5 Hotels nach Stadt, Sterne, Gästezahl, Zeitraum")
        print("1.6 Hotelinformationen anzeigen")
        print("0. Zurück zum Hauptmenü")
        auswahl = input("Option wählen: ")
        if auswahl == "1.1":
            user_story_1_1()
        elif auswahl == "1.2":
            user_story_1_2()
        elif auswahl == "1.3":
            user_story_1_3()
        elif auswahl == "1.4":
            user_story_1_4()
        elif auswahl == "1.5":
            user_story_1_5()
        elif auswahl == "1.6":
            user_story_1_6()
        elif auswahl == "0":
            break
        else:
            print("Ungültige Eingabe.")

def main_menu():
    while True:
        print("\n===== HOTELRESERVIERUNGSSYSTEM =====")
        print("1. Gast")
        print("2. Admin")
        print("0. Beenden")
        choice = input("Als wer möchten Sie fortfahren? ")
        if choice == "1":
            gast_menu()
        elif choice == "2":
            print("Admin-Menü wird noch entwickelt...")
        elif choice == "0":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe.")

if __name__ == "__main__":
    main_menu()