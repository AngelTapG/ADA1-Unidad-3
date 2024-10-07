class Pila:
    def __init__(self, nombre):
        self.items = []
        self.nombre = nombre

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop() if self.items else None

    def __str__(self):
        return f"{self.nombre}: {self.items}"

def mover_disco(origen, destino):
    disco = origen.desapilar()
    destino.apilar(disco)
    print(f"Mover disco {disco} de {origen.nombre} a {destino.nombre}")

def torres_hanoi(n, origen, auxiliar, destino):
    if n == 1:
        mover_disco(origen, destino)
    else:
        torres_hanoi(n - 1, origen, destino, auxiliar)
        mover_disco(origen, destino)
        torres_hanoi(n - 1, auxiliar, origen, destino)

# Configuración inicial
torre_a = Pila("A")
torre_b = Pila("B")
torre_c = Pila("C")

# Apilar 3 discos en la torre A
for i in range(3, 0, -1):
    torre_a.apilar(i)

print("Estado inicial:")
print(torre_a, torre_b, torre_c)

# Resolver el juego
print("\nPasos para resolver:")
torres_hanoi(3, torre_a, torre_b, torre_c)

print("\nEstado final:")
print(torre_a, torre_b, torre_c)