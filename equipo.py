class Equipo():
    def __init__(self, id: str, code: str, name: str, group: str) -> None:
        self.id = id
        self.code = code
        self.name = name
        self.group = group

    def __str__(self):
        return f"{self.name} - {self.code}"