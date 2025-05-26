from data_access.base_dal import BaseDAL
from model.invoice import Invoice

class InvoiceDAL(BaseDAL):
    def __init__(self):
        super().__init__()

    def get_by_id(self, invoice_id: int) -> Invoice | None:
        with self._connect() as conn:
            cursor = conn.execute("SELECT * FROM invoices WHERE invoice_id=?", (invoice_id,))
            row = cursor.fetchone()
        if row:
            return Invoice(
                invoice_id=row["invoice_id"],
                booking_id=row["booking_id"],
                issue_date=row["issue_date"],
                total_amount=row["total_amount"],
                is_paid=bool(row["is_paid"])
            )
        return None

    def get_by_booking_id(self, booking_id: int) -> Invoice | None:
        with self._connect() as conn:
            cursor = conn.execute("SELECT * FROM invoices WHERE booking_id=?", (booking_id,))
            row = cursor.fetchone()
        if row:
            return Invoice(
                invoice_id=row["invoice_id"],
                booking_id=row["booking_id"],
                issue_date=row["issue_date"],
                total_amount=row["total_amount"],
                is_paid=bool(row["is_paid"])
            )
        return None

    def get_all(self) -> list[Invoice]:
        with self._connect() as conn:
            cursor = conn.execute("SELECT * FROM invoices")
            rows = cursor.fetchall()
        return [
            Invoice(
                invoice_id=row["invoice_id"],
                booking_id=row["booking_id"],
                issue_date=row["issue_date"],
                total_amount=row["total_amount"],
                is_paid=bool(row["is_paid"])
            ) for row in rows
        ]

    def create(self, invoice: Invoice) -> Invoice:
        with self._connect() as conn:
            cursor = conn.execute(
                "INSERT INTO invoices (booking_id, issue_date, total_amount, is_paid) VALUES (?, ?, ?, ?)",
                (invoice.booking_id, invoice.issue_date, invoice.total_amount, 1 if invoice.is_paid else 0)
            )
            conn.commit()
            invoice.invoice_id = cursor.lastrowid
        return invoice

    def update(self, invoice: Invoice) -> bool:
        with self._connect() as conn:
            result = conn.execute(
                "UPDATE invoices SET booking_id=?, issue_date=?, total_amount=?, is_paid=? WHERE invoice_id=?",
                (invoice.booking_id, invoice.issue_date, invoice.total_amount, 1 if invoice.is_paid else 0, invoice.invoice_id)
            )
            conn.commit()
        return result.rowcount > 0

    def delete(self, invoice_id: int) -> bool:
        with self._connect() as conn:
            result = conn.execute("DELETE FROM invoices WHERE invoice_id=?", (invoice_id,))
            conn.commit()
        return result.rowcount > 0