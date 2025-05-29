from data_access.base_dal import BaseDAL
from model.room import Room

class RoomDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def get_by_id(self, room_id: int) -> Room | None:
        sql = "SELECT * FROM room WHERE room_id = ?"
        with self._connect() as conn:
            cursor = conn.execute(sql, (room_id,))
            row = cursor.fetchone()
        if row:
            return Room(
                room_id=row[0],
                hotel_id=row[1],
                room_no=row[2],
                type_id=row[3],
                price_per_night=row[4]
            )
        return None

    def get_rooms_by_hotel_id(self, hotel_id: int) -> list[Room]:
        sql = "SELECT * FROM room WHERE hotel_id = ?"
        with self._connect() as conn:
            cursor = conn.execute(sql, (hotel_id,))
            rows = cursor.fetchall()
        return [
            Room(
                room_id=row[0],
                hotel_id=row[1],
                room_no=row[2],
                type_id=row[3],
                price_per_night=row[4]
            )
            for row in rows
        ]

    def get_all_rooms(self) -> list[Room]:
        sql = "SELECT * FROM room"
        with self._connect() as conn:
            cursor = conn.execute(sql)
            rows = cursor.fetchall()
        return [
            Room(
                room_id=row[0],
                hotel_id=row[1],
                room_no=row[2],
                type_id=row[3],
                price_per_night=row[4]
            )
            for row in rows
        ]
    

    def get_booked_room_ids(self, hotel_id: int, check_in: str, check_out: str) -> list[int]:
        sql = """
            SELECT DISTINCT r.room_id
            FROM room r
            JOIN booking b ON r.room_id = b.room_id
            WHERE r.hotel_id = ?
            AND b.is_cancelled = 0
            AND (
                (b.check_in_date < ? AND b.check_out_date > ?) OR
                (b.check_in_date >= ? AND b.check_in_date < ?)
            )
        """
        with self._connect() as conn:
            cursor = conn.execute(sql, (hotel_id, check_out, check_in, check_in, check_out))
            rows = cursor.fetchall()
        return [row[0] for row in rows]
    
    def create_room(self, hotel_id: int, room_no: str, type_id: int, price_per_night: float) -> int:
        sql = "INSERT INTO room (hotel_id, room_number, type_id, price_per_night) VALUES (?, ?, ?, ?)"
        params = (hotel_id, room_no, type_id, price_per_night)
        return self.insert_and_get_id(sql, params)
    
    def insert_and_get_id(self, sql: str, params: tuple) -> Room:
        with self._connect() as conn:
            cursor = conn.execute(sql, params)
            conn.commit()
            last_row_id = cursor.lastrowid
        return last_row_id #Room(room_id=last_row_id, hotel_id=params[0], room_no=params[1], type_id=params[2], price_per_night=params[3])
    
    def get_next_room_number(self, hotel_id: int) -> str:
        sql = "SELECT room_number FROM room WHERE hotel_id = ?"
        with self._connect() as conn:
            cursor = conn.execute(sql, (hotel_id,))
            rows = cursor.fetchall()

        max_number = 0
        for row in rows:
            try:
                num = int(row["room_number"])
                max_number = max(max_number, num)
            except (ValueError, TypeError):
                continue

        return str(max_number + 1).zfill(3)
    
    def get_rooms_with_facilities(self) -> list[dict]:
        # SQL query to get rooms with their hotel name, type, price and facilities
        sql = """
            SELECT r.room_id, r.room_number, r.hotel_id, rt.description AS room_type, r.price_per_night,
                h.name AS hotel_name,
                GROUP_CONCAT(f.facility_name, ', ') AS facilities
            FROM room r
            JOIN room_type rt ON r.type_id = rt.type_id
            JOIN hotel h ON r.hotel_id = h.hotel_id
            LEFT JOIN room_facilities rf ON r.room_id = rf.room_id
            LEFT JOIN facilities f ON rf.facility_id = f.facility_id
            GROUP BY r.room_id
            ORDER BY h.name, r.room_number
        """
        # connect to the database and run the query
        with self._connect() as conn:
            cursor = conn.execute(sql)
            rows = cursor.fetchall()
        # build a list of dictionaries with room details
        return [
            {
                "room_id": row["room_id"],
                "room_number": row["room_number"],
                "hotel_name": row["hotel_name"],
                "room_type": row["room_type"],
                "price_per_night": row["price_per_night"],
                "facilities": row["facilities"] or "Keine"  # fallback if no facilities
            }
            for row in rows
        ]