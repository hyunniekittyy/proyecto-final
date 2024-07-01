class Estadio():
    def __init__(self, id: str,name: str,city: str,capacity: list[int],restaurantes: list) -> None:
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurantes = restaurantes
    
    def __str__(self):
        return f'name: {self.name}'