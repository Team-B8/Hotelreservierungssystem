from data_access.base_dal import BaseDAL
from model.invoice import Invoice

class InvoiceDAL(BaseDAL):
    """Data access layer for the invoices table."""
    def get_by_id(self, invoice_id: int) -> Invoice:
        cursor = self.conn.execute("SELECT * FROM invoices WHERE id=?", (invoice_id,))
        row = cursor.fetchone()
        if row:
            return Invoice(**row)
        return None

    def get_by_booking_id(self, booking_id: int) -> Invoice:
        cursor = self.conn.execute("SELECT * FROM invoices WHERE booking_id=?", (booking_id,))
        row = cursor.fetchone()
        if row:
            return Invoice(**row)
        return None

    def get_all(self) -> list[Invoice]:
        cursor = self.conn.execute("SELECT * FROM invoices")
        rows = cursor.fetchall()
        return [Invoice(**row) for row in rows]

    def create(self, invoice: Invoice) -> Invoice:
        cursor = self.conn.execute(
            "INSERT INTO invoices (booking_id, amount, paid) VALUES (?, ?, ?)",
            (invoice.booking_id, invoice.amount, 1 if invoice.paid else 0)
        )
        self.conn.commit()
        invoice.id = cursor.lastrowid
        return invoice

    def update(self, invoice: Invoice) -> bool:
        result = self.conn.execute(
            "UPDATE invoices SET booking_id=?, amount=?, paid=? WHERE id=?",
            (invoice.booking_id, invoice.amount, 1 if invoice.paid else 0, invoice.id)
        )
        self.conn.commit()
        return result.rowcount > 0

    def delete(self, invoice_id: int) -> bool:
        result = self.conn.execute("DELETE FROM invoices WHERE id=?", (invoice_id,))
        self.conn.commit()
        return result.rowcount > 0