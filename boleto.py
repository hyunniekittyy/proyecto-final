from partido import Partido


class Boleto:
    def __init__(self, asiento: int, cliente_ci: int, partido: Partido) -> None:
        self.precio = 0
        self.asiento = asiento
        self.cliente_ci = cliente_ci
        self.partido = partido

class Boleto_vip(Boleto):
    def __init__(self, asiento: int, cliente_ci: int, partido: Partido) -> None:
        super().__init__(asiento, cliente_ci)
        self.precio = 75
        self.asiento = asiento
        self.cliente_ci = cliente_ci
        self.partido = partido
        


class Boleto_general(Boleto):
    def __init__(self, asiento: int, cliente_ci: int, partido: Partido) -> None:
        super().__init__(asiento, cliente_ci)
        self.precio = 35
        self.asiento = asiento
        self.cliente_ci = cliente_ci
        self.partido = partido
        