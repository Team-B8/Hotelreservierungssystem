import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from business_logic.hotel_manager import HotelManager
from datetime import datetime
from business_logic.room_manager import RoomManager
from business_logic.room_type_manager import RoomTypeManager
from business_logic.facilities_manager import FacilitiesManager

def input_date(prompt):
    while True:
        try:
            return datetime.strptime(input(prompt + ' (YYYY-MM-DD): '), "%Y-%m-%d").date()
        except ValueError:
            print("Ungültiges Datum. Bitte erneut eingeben.")

def user_story_1_1():
    # Print the title of the feature
    print("\n--- 1.1: Hotels nach Stadt filtern ---")
    # Ask the user to enter a city name
    city = input("Stadt eingeben: ")
    # Get hotels in the entered city using HotelManager
    hotels = HotelManager().filter_by_city(city)
    # Print info about each hotel
    for hotel in hotels:
        print(f"ID: {hotel.hotel_id} | Name: {hotel.name} | Sterne: {hotel.stars}")

def user_story_1_2():
    # print the title for this user story
    print("\n--- 1.2: Hotels nach Sternen in Stadt filtern ---")
    # ask user to enter a city
    city = input("Stadt eingeben: ")
    # ask user to enter the minimum number of stars
    min_stars = int(input("Minimale Sterne (1–5): "))
    # get hotels that match the city and have at least the given stars
    hotels = HotelManager().filter_by_city_and_stars(city, min_stars)
    # print info about each hotel
    for hotel in hotels:
        print(f"ID: {hotel.hotel_id} | Name: {hotel.name} | Sterne: {hotel.stars}")

def user_story_1_3():
    # print the title for this user story
    print("\n--- 1.3: Hotels mit passenden Zimmern für Gästezahl in Stadt ---")
    # ask user for a city
    city = input("Stadt: ")
    # ask user for number of guests
    guests = int(input("Anzahl Gäste: "))
    # get hotels in the city that have rooms for the given number of guests
    hotels = HotelManager().filter_by_city_and_guest_capacity(city, guests)
    # print hotel name and stars for each result
    for hotel in hotels:
        print(f"Hotel: {hotel.name} | Sterne: {hotel.stars}")

def user_story_1_4():
    # print the title for this user story
    print("\n--- 1.4: Hotels mit verfügbaren Zimmern im Zeitraum ---")
    # ask user for a city
    city = input("Stadt: ")
    # get check-in date from user
    check_in = input_date("Check-in Datum")
    # get check-out date from user
    check_out = input_date("Check-out Datum")
    # get hotels in the city that have free rooms in the given time period
    hotels = HotelManager().filter_by_availability(city, check_in, check_out)
    # print hotel name and stars
    for hotel in hotels:
        print(f"Hotel: {hotel.name} | Sterne: {hotel.stars}")

def user_story_1_5():
    # print the title for this user story
    print("\n--- 1.5: Kombinierte Suche (Stadt, Gästezahl, Sterne, Zeitraum) ---")
    # ask user for input data
    city = input("Stadt: ")
    guests = int(input("Anzahl Gäste: "))
    stars = int(input("Minimale Sterne: "))
    check_in = input_date("Check-in Datum")
    check_out = input_date("Check-out Datum")
    # get hotels that match all filters
    hotels = HotelManager().filter_combined(city, guests, stars, check_in, check_out)
    # print hotel info
    for hotel in hotels:
        print(f"Hotel: {hotel.name} | Sterne: {hotel.stars}")


def user_story_1_6():
    # print the title for this user story
    print("\n--- 1.6: Hotelinformationen anzeigen ---")
    # get all hotels from the HotelManager
    hotels = HotelManager().get_all_hotels()
    # print info for each hotel
    for hotel in hotels:
        # get the address for the current hotel
        address = HotelManager().address_dal.get_address_by_hotel(hotel.hotel_id)
        # print hotel name, stars, and full address
        print(f"{hotel.name} | {hotel.stars} Sterne | Adresse: {address.get_full_address()}")

def user_story_2_1():
    # print the title for this user story
    print("\n--- 2.1: Zimmerdetails anzeigen ---")
    # show all available hotels
    hotels = HotelManager().get_all_hotels()
    print("\nVerfügbare Hotels:")
    for h in hotels:
        print(f"- {h.name}")
    # ask user to enter hotel naﬁme
    hotel_name = input("Hotelname eingeben: ")
    hotel = HotelManager().get_hotel_by_name(hotel_name)
    if not hotel:
        print("Hotel nicht gefunden.")
        return
    hotel_id = hotel.hotel_id
    # ask user for check-in and check-out date
    check_in = input_date("Check-in Datum")
    check_out = input_date("Check-out Datum")
    # check that check_out is after check_in
    if check_out <= check_in:
        print("Check-out muss nach dem Check-in liegen.")
        return
    # get all rooms for the given hotel
    rooms = RoomManager().get_rooms_by_hotel_id(hotel_id)
    # print details for each room
    for room in rooms:
        # get room type for room
        room_type = RoomTypeManager().get_by_id(room.type_id)
        # get facilities for room
        facilities = FacilitiesManager().get_facilities_for_room(room.room_id)
        # calculate total price for the stay
        nights = (check_out - check_in).days
        total_price = nights * room.price_per_night
        # print room information
        print(f"\nRoom No: {room.room_no}")
        print(f"Type: {room_type.description} | Max Guests: {room_type.max_guests}")
        print(f"Price per night: {room.price_per_night} | Total price: {total_price}")
        print("Facilities: " + ", ".join([f.facility_name for f in facilities]))

def user_story_2_2():
    # print the title for this user story
    print("\n--- 2.2: Verfügbare Zimmer anzeigen ---")
    # show all available hotels
    hotels = HotelManager().get_all_hotels()
    print("\nVerfügbare Hotels:")
    for h in hotels:
        print(f"- {h.name}")
    # ask user to enter hotel name
    hotel_name = input("Hotelname eingeben: ")
    hotel = HotelManager().get_hotel_by_name(hotel_name)
    if not hotel:
        print("Hotel nicht gefunden.")
        return
    hotel_id = hotel.hotel_id
    # ask user for check-in and check-out date
    check_in = input_date("Check-in Datum")
    check_out = input_date("Check-out Datum")
    # check that check_out is after check_in
    if check_out <= check_in:
        print("Check-out muss nach dem Check-in liegen.")
        return
    # get detailed available rooms
    rooms = RoomManager().get_detailed_available_rooms(hotel_id, str(check_in), str(check_out))
    if not rooms:
        print("Keine verfügbaren Zimmer gefunden.")
        return
    for room in rooms:
        # get room type for room
        room_type = RoomTypeManager().get_by_id(room.type_id)
        # get facilities for room
        facilities = FacilitiesManager().get_facilities_for_room(room.room_id)
        # calculate total price for the stay
        nights = (check_out - check_in).days
        total_price = nights * room.price_per_night
        # print room information
        print(f"\nRoom No: {room.room_no}")
        print(f"Type: {room_type.description} | Max Guests: {room_type.max_guests}")
        print(f"Price per night: {room.price_per_night} | Total price: {total_price}")
        print("Facilities: " + ", ".join([f.facility_name for f in facilities]))
    
    def user_story_3_1():
        # print the title for this user story
        print("\n--- 3.1: Hotel hinzufügen ---")
        # get hotel name and star rating from user
        name = input("Hotelname: ")
        stars = int(input("Sterne (1–5): "))
        try:
            # try to create the hotel using HotelManager
            hotel = HotelManager().create_hotel(name, stars)
            # print success message with hotel name and ID
            print(f"Hotel '{hotel.name}' mit ID {hotel.hotel_id} hinzugefügt.")
        except Exception as e:
            # print error message if something goes wrong
            print(f"Fehler beim Hinzufügen des Hotels: {e}")


def gast_menu():
    while True:
        print("\n--- GAST MENÜ ---")
        print("1.1 Hotels nach Stadt filtern")
        print("1.2 Hotels nach Sternen in Stadt filtern")
        print("1.3 Hotels mit passenden Zimmern für Gästezahl")
        print("1.4 Hotels mit verfügbaren Zimmern im Zeitraum")
        print("1.5 Hotels nach Stadt, Sterne, Gästezahl, Zeitraum")
        print("1.6 Hotelinformationen anzeigen")
        print("2.1 Zimmerdetails anzeigen")
        print("2.2 Verfügbare Zimmer anzeigen")
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
        elif auswahl == "2.1":
            user_story_2_1()
        elif auswahl == "2.2":
            user_story_2_2()
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