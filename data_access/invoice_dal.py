from data_access.base_dal import BaseDal
from model.invoice import Invoice
from datetime import date

class InvoiceDAL(BaseDal):
    def create_invoice(self, booking_id: int, issue_date: date, total_amount: float, is_paid: bool = False) -> Invoice:
        sql = """
            INSERT INTO Invoice (booking_id, issue_date, total_amount, is_paid)
            VALUES (?, ?, ?, ?)
        """
        params = (booking_id, issue_date, total_amount, int(is_paid))
        last_id, _ = self.execute(sql, params)
        return Invoice(last_id, booking_id, issue_date, total_amount, is_paid)

    def get_invoice_by_id(self, invoice_id: int) -> Invoice | None:
        sql = "SELECT invoice_id, booking_id, issue_date, total_amount, is_paid FROM Invoice WHERE invoice_id = ?"
        result = self.fetchone(sql, (invoice_id,))
        if result:
            invoice_id, booking_id, issue_date, total_amount, is_paid = result
            return Invoice(invoice_id, booking_id, issue_date, total_amount, bool(is_paid))
        return None

    def mark_as_paid(self, invoice_id: int):
        sql = "UPDATE Invoice SET is_paid = 1 WHERE invoice_id = ?"
        self.execute(sql, (invoice_id,))
