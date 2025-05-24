#22/05/2025
#Brandon Morales

class TarjetaCredito:
    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self  # para permitir encadenamiento

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self  # para permitir encadenamiento

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar:.2f}")
        return self  # para permitir encadenamiento

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self  # para permitir encadenamiento

# Crear tarjetas

# Tarjeta 1: 2 compras, 1 pago, intereses, mostrar info
tarjeta1 = TarjetaCredito(limite_credito=1000, intereses=0.02)
tarjeta1.compra(200).compra(150).pago(100).cobrar_interes().mostrar_info_tarjeta()

# Tarjeta 2: 3 compras, 2 pagos, intereses, mostrar info
tarjeta2 = TarjetaCredito(limite_credito=2000, intereses=0.03)
tarjeta2.compra(300).compra(400).compra(250).pago(200).pago(100).cobrar_interes().mostrar_info_tarjeta()

# Tarjeta 3: 5 compras, exceder límite, mostrar info
tarjeta3 = TarjetaCredito(limite_credito=500, intereses=0.05)
tarjeta3.compra(100).compra(100).compra(100).compra(100).compra(200).mostrar_info_tarjeta()
