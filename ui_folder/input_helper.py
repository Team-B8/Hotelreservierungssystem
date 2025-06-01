import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime
from business_logic.room_manager import RoomManager
from business_logic.room_type_manager import RoomTypeManager
from business_logic.facilities_manager import FacilitiesManager
from business_logic.address_manager import AddressManager
from business_logic.hotel_manager import HotelManager
from business_logic.booking_manager import BookingManager
from business_logic.invoice_manager import InvoiceManager

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
        print(f"{h.hotel_id}: {h.name} ({h.stars} Sterne)")
    try:
        hotel_id = int(input("Hotel-ID eingeben: "))
        hotel = HotelManager().get_hotel(hotel_id)
        if not hotel:
            print("Hotel nicht gefunden.")
            return
    except ValueError:
        print("Ungültige Eingabe.")
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
        total_price = InvoiceManager().calculate_dynamic_price(room.price_per_night, check_in, check_out)
        season_hint = " (inkl. Hochsaisonaufschlag)" if check_in.month in [6, 7, 8] else " (inkl. Nebensaisonrabatt)" if check_in.month in [1, 2, 11] else ""
        # print room information
        print(f"\nRaum Nummer: {room.room_no}")
        print(f"Type: {room_type.description} | Maximale Anzahl Gäste: {room_type.max_guests}")
        print(f"Preis pro Nacht: {room.price_per_night} | Totaler Preis: {total_price}{season_hint}")
        print("Einrichtungen: " + ", ".join([f.facility_name for f in facilities]))

def user_story_2_2():
    # print the title for this user story
    print("\n--- 2.2: Verfügbare Zimmer anzeigen ---")
    # show all available hotels
    hotels = HotelManager().get_all_hotels()
    print("\nVerfügbare Hotels:")
    for h in hotels:
        print(f"{h.hotel_id}: {h.name} ({h.stars} Sterne)")
    try:
        hotel_id = int(input("Hotel-ID eingeben: "))
        hotel = HotelManager().get_hotel(hotel_id)
        if not hotel:
            print("Hotel nicht gefunden.")
            return
    except ValueError:
        print("Ungültige Eingabe.")
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
        total_price = InvoiceManager().calculate_dynamic_price(room.price_per_night, check_in, check_out)
        season_hint = " (inkl. Hochsaisonaufschlag)" if check_in.month in [6, 7, 8] else " (inkl. Nebensaisonrabatt)" if check_in.month in [1, 2, 11] else ""
        # print room information
        print(f"\nRaum Nummer: {room.room_no}")
        print(f"Type: {room_type.description} | Maximale Anzahl Gäste: {room_type.max_guests}")
        print(f"Preis pro Nacht: {room.price_per_night} | Totaler Preis: {total_price}{season_hint}")
        print("Einrichtungen: " + ", ".join([f.facility_name for f in facilities]))
    
def user_story_3_1():
    # print the title for this user story
    print("\n--- 3.1: Hotel hinzufügen ---")
    # get hotel name and star rating from user
    name = input("Hotelname: ")
    stars = int(input("Sterne (1–5): "))
    # get address details
    street = input("Strasse: ")
    city = input("Stadt: ")
    zip_code = input("PLZ: ")
    try:
        # create address and get id
        address = AddressManager().create_address(street, city, zip_code)
        # create hotel with the address
        hotel = HotelManager().create_hotel(name, stars, address.address_id)
        print(f"Hotel '{name}' erfolgreich hinzugefügt.")
        # add a room for the hotel
        print("\n--- Zimmer für das Hotel hinzufügen ---")
        # print room types
        room_types = RoomTypeManager().get_all()
        print("Verfügbare Zimmertypen:")
        for rt in room_types:
            print(f"{rt.type_id}: {rt.description} (max {rt.max_guests} Gäste)")
        type_id = int(input("Typ-ID wählen: "))
        price = float(input("Preis pro Nacht: "))
        try:
            room = RoomManager().create_room(hotel.hotel_id, type_id, price)
            print(f"Zimmer Nr. {room.room_no} erfolgreich hinzugefügt.")
            print("Zimmer erfolgreich hinzugefügt.")
        except Exception as e:
            print(f"Fehler beim Hinzufügen des Zimmers: {e}")

    except Exception as e:
        print(f"Fehler beim Hinzufügen des Hotels: {e}")

def user_story_3_2():
    # print the title for this user story
    print("\n--- 3.2: Hotel löschen ---")
    # show all hotels with ID and stars
    hotels = HotelManager().get_all_hotels()
    for h in hotels:
        print(f"{h.hotel_id}: {h.name} ({h.stars} Sterne)")
    try:
        # ask user for hotel ID to delete
        hotel_id = int(input("ID des zu löschenden Hotels eingeben: "))
        # get the hotel by ID
        hotel = HotelManager().get_hotel(hotel_id)
        if not hotel:
            print("Hotel nicht gefunden.")
            return
        # delete the hotel
        # confirm before deletion
        confirm = input(f"Bist du sicher, dass du das Hotel '{hotel.name}' löschen möchtest? (y/n): ").lower()
        if confirm == "y":
            HotelManager().delete_hotel(hotel_id)
            print(f"Hotel '{hotel.name}' wurde gelöscht.")
        else:
            print("Löschen abgebrochen.")
    except ValueError:
        # if user input is not a number
        print("Ungültige Eingabe. Bitte eine Zahl eingeben.")

def user_story_3_3():
    # print the title for this user story
    print("\n--- 3.3: Hotelinformationen aktualisieren ---")
    # show all hotels with ID and stars
    hotels = HotelManager().get_all_hotels()
    for h in hotels:
        print(f"{h.hotel_id}: {h.name} ({h.stars} Sterne)")
    try:
        # ask user for hotel ID to update
        hotel_id = int(input("ID des zu bearbeitenden Hotels eingeben: "))
        manager = HotelManager()
        hotel = manager.get_hotel(hotel_id)
        # check if hotel exists
        if not hotel:
            print("Hotel nicht gefunden.")
            return
        # get the current address of the hotel
        address = manager.address_dal.get_address_by_hotel(hotel_id)
        # show current hotel info
        print(f"Aktuell: Name: {hotel.name}, Sterne: {hotel.stars}")
        print(f"Adresse: {address.street}, {address.zip_code} {address.city}")
        # get new name and stars from user input
        new_name = input("Neuer Hotelname (leer lassen für keine Änderung): ")
        new_stars_input = input("Neue Sternezahl (1–5, leer lassen für keine Änderung): ")
        # get new address data from user input
        new_street = input("Neue Straße (leer lassen für keine Änderung): ")
        new_zip = input("Neue PLZ (leer lassen für keine Änderung): ")
        new_city = input("Neue Stadt (leer lassen für keine Änderung): ")
        # keep old values if input is empty
        new_name = new_name if new_name.strip() else hotel.name
        new_stars = int(new_stars_input) if new_stars_input.strip() else hotel.stars
        address.street = new_street if new_street.strip() else address.street
        address.zip_code = new_zip if new_zip.strip() else address.zip_code
        address.city = new_city if new_city.strip() else address.city
        # update hotel and address in the database
        updated = manager.update_hotel(hotel_id, new_name, new_stars)
        manager.address_dal.update_address(address)
        # show result message
        if updated:
            print("Hotel und Adresse erfolgreich aktualisiert.")
        else:
            print("Hotel konnte nicht aktualisiert werden.")
    except ValueError:
        # handle invalid input
        print("Ungültige Eingabe. Bitte gültige Werte eingeben.")

def user_story_4():
    # print the title for this user story
    print("\n--- 4: Zimmer buchen ---")
    # show available hotels
    hotels = HotelManager().get_all_hotels()
    print("Verfügbare Hotels:")
    for h in hotels:
        print(f"{h.hotel_id}: {h.name}")
    try:
        # ask user to select a hotel and enter booking dates
        hotel_id = int(input("Hotel-ID auswählen: "))
        check_in = input_date("Check-in Datum")
        check_out = input_date("Check-out Datum")
        # check if check-out is after check-in
        if check_out <= check_in:
            print("Check-out muss nach dem Check-in liegen.")
            return
        # get available rooms for the hotel and date range
        available_rooms = RoomManager().get_available_rooms_by_hotel_and_dates(
            hotel_id, str(check_in), str(check_out)
        )
        # if no rooms available, show message
        if not available_rooms:
            print("Keine verfügbaren Zimmer für den Zeitraum.")
            return
        # show available rooms
        print("Verfügbare Zimmer:")
        for room in available_rooms:
            print(f"{room.room_id}: Zimmer Nr. {room.room_no}, Preis: {room.price_per_night} CHF")
        # user selects a room to book
        room_id = int(input("Zimmer-ID zum Buchen wählen: "))
        # ask if user already has an account
        print("\nHaben Sie bereits ein Konto?")
        has_account = input("Ja (j) / Nein (n): ").strip().lower()
        # create booking and invoice manager
        invoice_manager = InvoiceManager()
        booking_manager = BookingManager(invoice_manager)
        room = RoomManager().get_room_by_id(room_id)
        total_amount = InvoiceManager().calculate_dynamic_price(room.price_per_night, check_in, check_out)
        if has_account == "j":
            # existing guest: ask for email only
            email = input("Bitte geben Sie Ihre E-Mail-Adresse ein: ").strip()
            booking = booking_manager.create_booking_existing_guest(room_id, check_in, check_out, email, total_amount)
        else:
            # new guest: collect full registration data
            print("\n--- Registrierung ---")
            first_name = input("Vorname: ")
            last_name = input("Nachname: ")
            email = input("E-Mail: ")
            street = input("Strasse: ")
            city = input("Stadt: ")
            zip_code = input("PLZ: ")
            booking = booking_manager.create_booking_new_guest(room_id, check_in, check_out, first_name, last_name, email, street, city, zip_code, total_amount)
        # show booking success and create invoice
        print(f"Buchung erfolgreich! Buchungs-ID: {booking.booking_id}")
        invoice = invoice_manager.generate_invoice(booking)
        print(f"Rechnung erstellt. Betrag: {invoice.total_amount:.2f} CHF")
    except Exception as e:
        # show error if something goes wrong
        print(f"Fehler bei der Buchung: {e}")

def user_story_5():
    # print the title for this user story
    print("\n--- 5: Rechnung abrufen ---")
    try:
        # ask user how they want to search for invoice
        wahl = input("Rechnung suchen nach: (1) E-Mail oder (2) Buchungs-ID: ").strip()
        if wahl == "1":
            # search by email
            email = input("E-Mail eingeben: ")
            invoices = InvoiceManager().get_invoices_by_email(email)
            # if no invoices found
            if not invoices:
                print("Keine Rechnungen gefunden.")
                return           
            # show all found invoices
            for invoice in invoices:
                print(f"\nRechnungs-ID: {invoice.invoice_id}")
                print(f"Buchungs-ID: {invoice.booking_id}")
                print(f"Betrag: {invoice.total_amount:.2f} CHF")
                print(f"Datum: {invoice.issue_date}")
                print(f"Storniert: {'Ja' if invoice.is_cancelled else 'Nein'}")
        elif wahl == "2":
            # search by booking ID
            booking_id = int(input("Buchungs-ID eingeben: "))
            invoice = InvoiceManager().get_invoice_by_booking_id(booking_id)
            # if invoice not found
            if not invoice:
                print("Keine Rechnung gefunden.")
                return
            # show invoice details
            print(f"\nRechnungs-ID: {invoice.invoice_id}")
            print(f"Buchungs-ID: {invoice.booking_id}")
            print(f"Betrag: {invoice.total_amount:.2f} CHF")
            print(f"Datum: {invoice.issue_date}")
            print(f"Storniert: {'Ja' if invoice.is_cancelled else 'Nein'}")
    except Exception as e:
        # show error message if something goes wrong
        print(f"Fehler beim Abrufen der Rechnung: {e}")

def user_story_6():
    # print the title for this user story
    print("\n--- 6: Buchung stornieren ---")
    try:
        # ask user for the booking ID
        booking_id = int(input("Bitte geben Sie Ihre Buchungs-ID ein: "))
        # confirm cancellation
        confirm = input("Sind Sie sicher, dass Sie diese Buchung stornieren möchten? (j/n): ").strip().lower()
        if confirm != "j":
            print("Stornierung abgebrochen.")
            return
        # create booking manager with invoice manager
        booking_manager = BookingManager(InvoiceManager())
        # try to cancel the booking
        success = booking_manager.cancel_booking(booking_id)
        # show result
        if success:
            print("Buchung und zugehörige Rechnung wurden erfolgreich storniert.")
        else:
            print("Buchung konnte nicht gefunden oder storniert werden.")
    # show error if something goes wrong
    except Exception as e:
        print(f"Fehler bei der Stornierung: {e}")

def user_story_8():
    # print the title for this user story
    print("\n--- 8: Alle Buchungen anzeigen ---")
    try:
        # get all bookings from the booking manager
        manager = BookingManager()
        bookings = manager.get_all_bookings_with_details()
        # if no bookings found, show message
        if not bookings:
            print("Keine Buchungen gefunden.")
            return
        # print details for each booking
        print("-" * 50)
        for b in bookings:
            booking_id, guest_name, room_no, hotel_name, check_in, check_out, total, is_cancelled = b
            status = "Storniert" if is_cancelled else "Aktiv"
            print(f"Buchung #{booking_id}: {guest_name} – {hotel_name}, Zimmer {room_no}")
            print(f"  Zeitraum: {check_in} bis {check_out}")
            print(f"  Betrag: {total:.2f} CHF – Status: {status}")
            print("-" * 50)
    except Exception as e:
        # show error message if something goes wrong
        print(f"Fehler beim Abrufen der Buchungen: {e}")

def user_story_9():
    # print the title for this user story
    print("\n--- 9: Zimmer und Ausstattung anzeigen ---")
    try:
        # get all data of rooms
        rooms_with_facilities = RoomManager().get_all_rooms_with_facilities()
        if not rooms_with_facilities:
            print("Keine Zimmer gefunden.")
            return
        # print every room with details
        for room in rooms_with_facilities:
            print(f"\nHotel: {room['hotel_name']}")
            print(f"Zimmernummer: {room['room_number']}")
            print(f"Typ: {room['room_type']}")
            print(f"Preis pro Nacht: {room['price_per_night']} CHF")
            print("Einrichtungen: " + (room['facilities'] or "Keine"))
    except Exception as e:
        print(f"Fehler beim Abrufen der Zimmerdaten: {e}")

def user_story_10():
    while True:
        # main menu for managing master data
        print("\n--- 10: Stammdaten verwalten ---")
        print("1 Zimmertypen verwalten")
        print("2 Einrichtungen verwalten")
        print("3 Zimmerpreise ändern")
        print("4 Saisonregeln anzeigen")
        print("0 Zurück")
        wahl = input("Menüpunkt wählen: ").strip()

        if wahl == "1":
            # room type management submenu
            while True:
                print("\n--- Zimmertypen ---")
                types = RoomTypeManager().get_all()
                for t in types:
                    print(f"{t.type_id}: {t.description} (max {t.max_guests} Gäste)")
                print("\na Hinzufügen")
                print("b Bearbeiten")
                print("c Löschen")
                print("z Zurück")
                action = input("Aktion wählen: ").strip().lower()
                manager = RoomTypeManager()
                
                if action == "a":
                    # add new room type
                    desc = input("Beschreibung: ")
                    try:
                        max_guests = int(input("Maximale Gästezahl: "))
                        manager.create_room_type(desc, max_guests)
                        print("Zimmertyp hinzugefügt.")
                    except Exception as e:
                        print(f"Fehler: {e}")
                
                elif action == "b":
                    # edit existing room type
                    try:
                        id = int(input("Typ-ID zum Bearbeiten: "))
                        manager = RoomTypeManager()
                        existing_type = manager.get_by_id(id)
                        if not existing_type:
                            print("Zimmertyp wurde nicht gefunden.")
                            continue
                        desc = input("Neue Beschreibung: ")
                        max_guests = int(input("Neue maximale Gästezahl: "))
                        manager.update_room_type(id, desc, max_guests)
                        print("Zimmertyp aktualisiert.")
                    except Exception as e:
                        print(f"Fehler: {e}")
                
                elif action == "c":
                    # delete room type if not in use
                    try:
                        id = int(input("Typ-ID zum Löschen: "))
                        manager = RoomTypeManager()
                        existing_type = manager.get_by_id(id)
                        if not existing_type:
                            print("Zimmertyp wurde nicht gefunden.")
                            continue
                        if manager.is_type_in_use(id):
                            print("Zimmertyp ist noch in Verwendung und kann nicht gelöscht werden.")
                        else:
                            manager.delete_room_type(id)
                            print("Zimmertyp gelöscht.")
                    except Exception as e:
                        print(f"Fehler: {e}")
                
                elif action == "z":
                    break  # back to main menu
                else:
                    print("Ungültige Eingabe.")

        elif wahl == "2":
            # facilities management submenu
            while True:
                print("\n--- Einrichtungen ---")
                facilities = FacilitiesManager().get_all_facilities()
                for f in facilities:
                    print(f"{f.facility_id}: {f.facility_name}")
                print("\na Hinzufügen")
                print("b Bearbeiten")
                print("c Löschen")
                print("z Zurück")
                action = input("Aktion wählen: ").strip().lower()
                manager = FacilitiesManager()
                
                if action == "a":
                    # add new facility
                    name = input("Einrichtungsname: ")
                    try:
                        manager.add_facility(name)
                        print("Einrichtung hinzugefügt.")
                    except Exception as e:
                        print(f"Fehler: {e}")
                
                elif action == "b":
                    # edit existing facility
                    try:
                        id = int(input("ID zum Bearbeiten: "))
                        manager = FacilitiesManager()
                        existing = manager.get_facility_by_id(id)
                        if not existing:
                            print("Einrichtung wurde nicht gefunden.")
                            continue                        
                        name = input("Neuer Name: ")
                        manager.update_facility(id, name)
                        print("Einrichtung aktualisiert.")
                    except Exception as e:
                        print(f"Fehler: {e}")
                
                elif action == "c":
                    # delete facility
                    try: 
                        id = int(input("ID zum Löschen: "))
                        manager = FacilitiesManager()
                        existing = manager.get_facility_by_id(id)
                        if not existing:
                            print("Einrichtung wurde nicht gefunden.")
                            continue
                        manager.delete_facility(id)
                        print("Einrichtung gelöscht.")
                    except Exception as e:
                        print(f"Fehler: {e}")
                
                elif action == "z":
                    break
                else:
                    print("Ungültige Eingabe.")

        elif wahl == "3":
            # update room price
            print("\n--- Zimmerpreise ändern ---")
            hotels = HotelManager().get_all_hotels()
            for h in hotels:
                print(f"{h.hotel_id}: {h.name}")
            try:
                hotel_id = int(input("Hotel-ID wählen: "))
                manager = HotelManager()
                existing = manager.get_hotel(id)
                if not existing:
                    print("Hotel wurde nicht gefunden.")
                    continue 
                rooms = RoomManager().get_rooms_by_hotel_id(hotel_id)
                for r in rooms:
                    print(f"{r.room_id}: Zimmer {r.room_no}, Preis: {r.price_per_night}")
                room_id = int(input("Zimmer-ID zum Bearbeiten: "))
                new_price = float(input("Neuer Preis pro Nacht: "))
                RoomManager().update_room_price(room_id, new_price)
                print("Zimmerpreis aktualisiert.")
            except Exception as e:
                print(f"Fehler: {e}")

        elif wahl == "4":
            # show current seasonal pricing rules
            print("\n--- Saisonregeln ---")
            print("Aktuell gelten folgende Regeln:")
            print("Hochsaison: Juni, Juli, August → +25%")
            print("Nebensaison: Januar, Februar, November → -15%")
            print("Normale Saison: alle übrigen Monate")

        elif wahl == "0":
            break  # exit the main menu
        else:
            print("Ungültige Eingabe.")

def user_story_data_visualization():
    import pandas as pd
    import matplotlib.pyplot as plt
    print("\n--- 11: Show occupancy rates per room type ---")
    try:
        # List all available hotels
        hotels = HotelManager().get_all_hotels()
        for h in hotels:
            print(f"{h.hotel_id}: {h.name}")
        # Prompt user to select a hotel
        hotel_id = int(input("Select Hotel ID: "))
        manager = BookingManager()
        # Get occupancy stats for the selected hotel
        stats = manager.get_room_type_occupancy_by_hotel(hotel_id)
        if not stats:
            print("No booking data available.")
            return
        # Load results into a pandas DataFrame
        df = pd.DataFrame(stats)
        # Display as text table in the terminal
        print("\nBooking statistics:")
        print(df.to_string(index=False))
        # Create a bar chart of occupancy counts by room type
        df.plot(kind="bar", x="room_type", y="count", legend=False)
        plt.title("Occupancy per Room Type")
        plt.xlabel("Room Type")
        plt.ylabel("Number of Bookings")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show() 
    except Exception as e:
        print(f"Error while retrieving occupancy rates: {e}")

def gast_menu():
    while True:
        print("\n--- GAST MENÜ ---")
        print("1 Hotels nach Stadt filtern")
        print("2 Hotels nach Sternen in Stadt filtern")
        print("3 Hotels mit passenden Zimmern für Gästezahl")
        print("4 Hotels mit verfügbaren Zimmern im Zeitraum")
        print("5 Hotels nach Stadt, Sterne, Gästezahl, Zeitraum")
        print("6 Hotelinformationen anzeigen")
        print("7 Zimmerdetails anzeigen")
        print("8 Verfügbare Zimmer anzeigen")
        print("9 Zimmer buchen")
        print("10 Rechnung abrufen")
        print("11 Buchung stornieren")
        print("0. Zurück zum Hauptmenü")
        auswahl = input("Menupunkt wählen: ")
        if auswahl == "1":
            user_story_1_1()
        elif auswahl == "2":
            user_story_1_2()
        elif auswahl == "3":
            user_story_1_3()
        elif auswahl == "4":
            user_story_1_4()
        elif auswahl == "5":
            user_story_1_5()
        elif auswahl == "6":
            user_story_1_6()
        elif auswahl == "7":
            user_story_2_1()
        elif auswahl == "8":
            user_story_2_2()
        elif auswahl == "9":
            user_story_4()
        elif auswahl == "10":
            user_story_5()
        elif auswahl == "11":
            user_story_6()
        elif auswahl == "0":
            break
        else:
            print("Ungültige Eingabe.")

def admin_menu():
    while True:
        print("\n--- ADMIN MENÜ ---")
        print("1 Hotel hinzufügen")
        print("2 Hotel löschen")
        print("3 Hotelinformationen aktualisieren")
        print("4 Alle Buchungen anzeigen")
        print("5 Zimmerdetails anzeigen")
        print("6 Stammdaten verwalten")
        print("7 Belegungsraten anzeigen")
        print("0. Zurück zum Hauptmenü")
        auswahl = input("Menupunkt wählen: ")
        if auswahl == "1":
            user_story_3_1()
        elif auswahl == "2":
            user_story_3_2()
        elif auswahl == "3":
            user_story_3_3()
        elif auswahl == "4":
            user_story_8()
        elif auswahl == "5":
            user_story_9()
        elif auswahl == "6":
            user_story_10()
        elif auswahl == "7":
            user_story_data_visualization()
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
            admin_menu()
        elif choice == "0":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe.")

if __name__ == "__main__":
    main_menu()