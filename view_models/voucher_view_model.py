from view_models.view_model import ViewModel


class VoucherViewModel(ViewModel):
    """Voucher view model which represents json parameter for sevDesk request"""
    def __init__(
        self,
        voucher_date,
        supplier_name,
        delivery_date,
        delivery_date_until,
        invoice_number,
        file_name
    ):
        super().__init__()
        self.voucher = {
            "voucherDate": voucher_date,
            "supplier": None,
            "supplierName": supplier_name,
            "status": 100,
            "voucherType": "VOU",
            "creditDebit": "D",
            "deliveryDate": delivery_date,
            "deliveryDateUntil": delivery_date_until,
            "description": invoice_number,
            "taxType": "default",
            "mapAll": True,
            "objectName": "Voucher"

        }
        self.voucherPosSave = []
        self.voucherPosDelete = None
        self.filename = file_name

    def add_voucher_position(self, voucher_position):
        """Add a new voucher position"""
        self.voucherPosSave.append(voucher_position.__dict__)
