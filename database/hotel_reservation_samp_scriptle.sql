CREATE TABLE Hotel (
	-- Author: AEP
    hotel_id       INTEGER PRIMARY KEY, 
    name           TEXT NOT NULL,
    stars          INTEGER,
    address_id     INTEGER NOT NULL,
    FOREIGN KEY (address_id) REFERENCES Address(address_id) ON DELETE SET NULL
);

CREATE TABLE Address (
	-- Author: AEP
    address_id     INTEGER PRIMARY KEY,
    street        TEXT NOT NULL,
    city          TEXT NOT NULL,
    zip_code      TEXT NOT NULL
);

CREATE TABLE Guest (
	-- Author: AEP
    guest_id       INTEGER PRIMARY KEY,
    first_name     TEXT NOT NULL,
    last_name      TEXT NOT NULL,
    email          TEXT NOT NULL UNIQUE,
    address_id     INTEGER NOT NULL,
    FOREIGN KEY (address_id) REFERENCES Address(address_id) ON DELETE SET NULL
);

CREATE TABLE Room_Type (
	-- Author: AEP
    type_id        INTEGER PRIMARY KEY,
    description    TEXT NOT NULL UNIQUE, -- E.g., Single, Double, Suite
    max_guests     INTEGER NOT NULL
);

CREATE TABLE Room (
	-- Author: AEP
    room_id        INTEGER PRIMARY KEY,
    hotel_id       INTEGER NOT NULL,
    room_number    TEXT NOT NULL,
    type_id        INTEGER NOT NULL,
    price_per_night REAL NOT NULL,
    FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES Room_Type(type_id) ON DELETE CASCADE
);

-- one-to-many mapping with guest, hotel, room
-- one booking can have only one room, but one room can be part of multiple bookings
-- if two rooms are booked for the same dates, two bookings should be created
-- check availability using business logic
CREATE TABLE Booking (
	-- Author: AEP
    booking_id     INTEGER PRIMARY KEY,
    guest_id       INTEGER NOT NULL,
    room_id        INTEGER NOT NULL,
    check_in_date  DATE NOT NULL,
    check_out_date DATE NOT NULL,
    is_cancelled   BOOLEAN NOT NULL DEFAULT 0, -- 0 = confirmed, 1 = cancelled
    total_amount   REAL NOT NULL,
    FOREIGN KEY (guest_id) REFERENCES Guest(guest_id) ON DELETE CASCADE,
    FOREIGN KEY (room_id) REFERENCES Room(room_id) ON DELETE CASCADE
);


CREATE TABLE Invoice (
	-- Author: AEP
    invoice_id     INTEGER PRIMARY KEY,
    booking_id     INTEGER NOT NULL,
    issue_date     DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total_amount   REAL NOT NULL,
    is_cancelled   BOOLEAN NOT NULL DEFAULT 0, -- 0 = confirmed, 1 = cancelled
    FOREIGN KEY (booking_id) REFERENCES Booking(booking_id) ON DELETE CASCADE
);

CREATE TABLE Facilities (
	-- Author: AEP
    facility_id   INTEGER PRIMARY KEY,
    facility_name TEXT NOT NULL UNIQUE -- E.g., "Shower", "TV", "WiFi", "Air Conditioning"
);

CREATE TABLE Room_Facilities (
	-- Author: AEP
    room_id       INTEGER NOT NULL,
    facility_id   INTEGER NOT NULL,
    PRIMARY KEY (room_id, facility_id),
    FOREIGN KEY (room_id) REFERENCES Room(room_id) ON DELETE CASCADE,
    FOREIGN KEY (facility_id) REFERENCES Facilities(facility_id) ON DELETE CASCADE
);

CREATE TABLE Rating (
	-- Author: Team 8
	rating_id    INTEGER PRIMARY KEY,
	guest_id     INTEGER NOT NULL,
	hotel_id     INTEGER NOT NULL,
	stars        INTEGER NOT NULL CHECK (stars BETWEEN 1 AND 5),
	comment      TEXT,
	created_date   DATE NOT NULL DEFAULT CURRENT_DATE,
	FOREIGN KEY (guest_id) REFERENCES Guest(guest_id) ON DELETE CASCADE,
	FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id) ON DELETE CASCADE
);

INSERT INTO Address (address_id, street, city, zip_code) VALUES
(1, 'Bahnhofstrasse 1', 'Zürich', '8001'),
(2, 'Rue du Rhône 42', 'Genève', '1204'),
(3, 'Pilatusstrasse 15', 'Luzern', '6003'),
(4, 'Marktgasse 59', 'Bern', '3011'),
(5, 'Freiestrasse 10', 'Basel', '4051');
(6, 'Via Nassa 3', 'Lugano', '6900'),
(7, 'Höhenweg 12', 'Interlaken', '3800'),
(8, 'Dorfstrasse 25', 'Zermatt', '3920');

INSERT INTO Hotel (hotel_id, name, stars, address_id) VALUES
(1, 'Hotel Baur au Lac', 5, 1),
(2, 'Four Seasons Hôtel des Bergues', 5, 2),
(3, 'Grand Hotel National', 5, 3),
(4, 'Bellevue Palace', 5, 4),
(5, 'Les Trois Rois', 5, 5);
(6, 'Hotel Splendide Royal', 5, 6),
(7, 'Victoria Jungfrau Grand Hotel', 5, 7),
(8, 'Mont Cervin Palace', 5, 8);

INSERT INTO Guest (guest_id, first_name, last_name, email, address_id) VALUES
(1, 'Hans', 'Müller', 'hans.mueller@example.ch', 1),
(2, 'Sophie', 'Meier', 'sophie.meier@example.ch', 2),
(3, 'Luca', 'Rossi', 'luca.rossi@example.ch', 3),
(4, 'Elena', 'Keller', 'elena.keller@example.ch', 4),
(5, 'Marc', 'Weber', 'marc.weber@example.ch', 5);
(6, 'Anna', 'Schmidt', 'anna.schmidt@example.ch', 6),
(7, 'Thomas', 'Fischer', 'thomas.fischer@example.ch', 7),
(8, 'Nina', 'Graf', 'nina.graf@example.ch', 8);


INSERT INTO Room_Type (type_id, description, max_guests) VALUES 
(1, 'Single', 1),
(2, 'Double', 2),
(3, 'Suite', 4),
(4, 'Family Room', 5),
(5, 'Penthouse', 6);


INSERT INTO Room (room_id, hotel_id, room_number, type_id, price_per_night) VALUES
(1, 1, '101', 1, 250.00),
(2, 1, '102', 2, 400.00),
(3, 2, '201', 3, 650.00),
(4, 3, '301', 4, 900.00),
(5, 4, '401', 5, 1500.00);
(6, 6, '601', 2, 420.00),
(7, 6, '602', 3, 750.00),
(8, 7, '701', 1, 230.00),
(9, 8, '801', 4, 890.00),
(10, 8, '802', 5, 1600.00);

INSERT INTO Booking (booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount) VALUES
(1, 1, 1, '2025-06-01', '2025-06-05', 0, 1000.00),
(2, 2, 2, '2025-07-10', '2025-07-15', 0, 2000.00),
(3, 3, 3, '2025-08-20', '2025-08-22', 0, 1300.00),
(4, 4, 4, '2025-09-05', '2025-09-10', 1, 0.00), -- Cancelled booking
(5, 5, 5, '2025-10-01', '2025-10-07', 0, 9000.00);
(6, 6, 6, '2025-06-12', '2025-06-15', 0, 1260.00),
(7, 7, 7, '2025-07-20', '2025-07-23', 0, 2250.00),
(8, 8, 8, '2025-08-05', '2025-08-10', 1, 0.00), -- Cancelled
(9, 6, 9, '2025-09-01', '2025-09-06', 0, 4450.00),
(10, 7, 10, '2025-09-10', '2025-09-12', 0, 3200.00);

INSERT INTO Invoice (invoice_id, booking_id, issue_date, total_amount, is_cancelled) VALUES
(1, 1, '2025-06-05', 1000.00, 0),
(2, 2, '2025-07-15', 2000.00, 0),
(3, 3, '2025-08-22', 1300.00, 0),
(4, 5, '2025-10-07', 9000.00, 0),
(5, 4, '2025-09-10', 0.00, 1); -- Cancelled booking, no charge
(6, 6, '2025-06-15', 1260.00, 0),
(7, 7, '2025-07-23', 2250.00, 0),
(8, 9, '2025-09-06', 4450.00, 0),
(9, 10, '2025-09-12', 3200.00, 0),
(10, 8, '2025-08-10', 0.00, 1); -- Cancelled booking, no charge

INSERT INTO Facilities (facility_id, facility_name) VALUES
(1, 'WiFi'),
(2, 'TV'),
(3, 'Air Conditioning'),
(4, 'Mini Bar'),
(5, 'Balcony');

INSERT INTO Room_Facilities (room_id, facility_id) VALUES
(1, 1), -- Room 101 has WiFi
(1, 2), -- Room 101 has TV
(2, 1), -- Room 102 has WiFi
(3, 3), -- Room 201 has Air Conditioning
(4, 4); -- Room 301 has Mini Bar
(6, 1), -- WiFi
(6, 3), -- Air Conditioning
(7, 1),
(7, 2),
(7, 4),
(8, 2),
(9, 1),
(9, 5),
(10, 1),
(10, 2),
(10, 3),
(10, 4),
(10, 5);

INSERT INTO Rating (rating_id, guest_id, hotel_id, stars, comment, created_date) VALUES
(1, 1, 1, 5, 'Wunderschönes Hotel mit hervorragendem Service.', '2025-06-06'),
(2, 2, 2, 4, 'Tolles Frühstück und zentrale Lage.', '2025-07-16'),
(3, 3, 3, 3, 'Schöne Aussicht, aber etwas laut in der Nacht.', '2025-08-23'),
(4, 5, 5, 5, 'Ein Erlebnis der Extraklasse. Uneingeschränkt empfehlenswert.', '2025-10-08');
(5, 6, 6, 4, 'Sehr elegantes Hotel mit wunderschönem Blick auf den See.', '2025-06-16'),
(6, 7, 7, 5, 'Fantastischer Spa-Bereich, gerne wieder.', '2025-07-24'),
(7, 6, 8, 5, 'Perfekte Lage in Zermatt, sehr luxuriös.', '2025-09-07');