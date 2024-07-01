class Producto:
    def __init__(self, name: str, quantity: int,price: str,stock: int,adicional: str) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price
        self.stock = stock
        self.adicional = adicional