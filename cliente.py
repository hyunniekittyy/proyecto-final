import itertools


class Cliente:
    def __init__(self, name: str, age: int, ci: int, password: str):
        self.name = name
        self.age = age
        self.ci = ci
        self.password = password
    
    def su_cedula_es_vampiro(self):
        cedula = self.ci
        lista = []
        for numero in str(cedula):
            lista.append(numero)
        permutations = list(itertools.permutations(lista))
        for permu in permutations:
            mitad = len("".join(permu)) // 2
            numero_1 = int("".join(permu[:mitad]))
            numero_2 = int("".join(permu[mitad:]))
    
            if numero_1*numero_2 == cedula:
                return True
        return False

