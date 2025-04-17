from datetime import datetime

class Comprobante:
    def __init__(self, tipo, proveedor, monto, fecha=None):
        self.tipo = tipo
        self.proveedor = proveedor
        self.monto = monto
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "tipo": self.tipo,
            "proveedor": self.proveedor,
            "monto": self.monto,
            "fecha": self.fecha
        }
