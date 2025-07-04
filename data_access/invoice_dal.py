from data_access.base_dal import BaseDAL
from model.invoice import Invoice

class InvoiceDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def get_by_booking_id(self, booking_id: int) -> Invoice | None:
        # Retrieves the invoice linked to a given booking_id returns None if no invoice is found
        with self._connect() as conn:
            cursor = conn.execute("SELECT * FROM Invoice WHERE booking_id=?", (booking_id,))
            row = cursor.fetchone()
        if row:
            return Invoice(
                invoice_id=row["invoice_id"],
                booking_id=row["booking_id"],
                issue_date=row["issue_date"],
                total_amount=row["total_amount"],
                is_cancelled=row["is_cancelled"]
            )
        return None

    def create(self, invoice: Invoice) -> Invoice:
        # Inserts a new invoice into the database and updates the invoice_id with the generated ID
        with self._connect() as conn:
            cursor = conn.execute(
                "INSERT INTO Invoice (booking_id, issue_date, total_amount, is_cancelled) VALUES (?, ?, ?, ?)",
                (invoice.booking_id, invoice.issue_date, invoice.total_amount, invoice.is_cancelled)
            )
            conn.commit()
            invoice.invoice_id = cursor.lastrowid
        return invoice

    def get_by_guest_email(self, email: str) -> list[Invoice]:
    # SQL query to get all invoices for a guest using their email
        sql = """SELECT i.invoice_id, i.booking_id, i.issue_date, i.total_amount, i.is_cancelled FROM Invoice i JOIN Booking b ON i.booking_id = b.booking_id JOIN Guest g ON b.guest_id = g.guest_id WHERE g.email = ?"""
        # connect to the database and run the query
        with self._connect() as conn:
            rows = conn.execute(sql, (email,)).fetchall()
        # convert each row to an Invoice object and return the list
        return [
            Invoice(
                invoice_id=row["invoice_id"],
                booking_id=row["booking_id"],
                issue_date=row["issue_date"],
                total_amount=row["total_amount"],
                is_cancelled=row["is_cancelled"]
            ) for row in rows
        ]

    def mark_invoice_as_cancelled(self, booking_id: int) -> bool:
        # SQL query to mark the invoice as cancelled by booking ID
        sql = "UPDATE Invoice SET is_cancelled = 1 WHERE booking_id = ?"
        # connect to the database and run the update
        with self._connect() as conn:
            cursor = conn.execute(sql, (booking_id,))
            conn.commit()
        # return True if at least one row was updated
        return cursor.rowcount > 0
    
    def get_all_by_date_and_hotel(self, start_date: str, end_date: str, hotel_id: int) -> list[Invoice]:
        # SQL query to get all invoices within a date range and for a specific hotel
        sql = """
        SELECT i.invoice_id, i.booking_id, i.issue_date, i.total_amount, i.is_cancelled
        FROM Invoice i
        JOIN Booking b ON i.booking_id = b.booking_id
        JOIN Room r ON b.room_id = r.room_id
        WHERE i.issue_date BETWEEN ? AND ? AND r.hotel_id = ?
        """
        # Connect to database and execute query
        with self._connect() as conn:
            rows = conn.execute(sql, (start_date, end_date, hotel_id)).fetchall()
        # Convert rows into Invoice objects and return the list
        return [
            Invoice(
                invoice_id=row["invoice_id"],
                booking_id=row["booking_id"],
                issue_date=row["issue_date"],
                total_amount=row["total_amount"],
                is_cancelled=row["is_cancelled"]
            ) for row in rows
        ]
