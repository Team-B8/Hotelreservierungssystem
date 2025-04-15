from data_access.invoice_dal import InvoiceDAL
from model.invoice import Invoice

class InvoiceManager:
    def __init__(self):
        # Initialize the data access layer for invoices
        self.__invoice_dal = InvoiceDAL()

    def get_invoice(self, invoice_id: int) -> Invoice | None:
        # Retrieve an invoice by its ID
        return self.__invoice_dal.get_invoice_by_id(invoice_id)

    def pay_invoice(self, invoice_id: int) -> None:
        # Mark the invoice with the given ID as paid
        self.__invoice_dal.mark_as_paid(invoice_id)
