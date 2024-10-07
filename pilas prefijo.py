class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

def es_operador(token):
    return token in set(['+', '-', '*', '/'])

def aplicar_operador(operador, a, b):
    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        return a / b

def evaluar_posfija(expresion):
    pila = Pila()
    
    for token in expresion.split():
        if not es_operador(token):
            pila.apilar(float(token))
        else:
            b = pila.desapilar()
            a = pila.desapilar()
            pila.apilar(aplicar_operador(token, a, b))
    
    return pila.desapilar()

def evaluar_prefija(expresion):
    pila = Pila()
    
    for token in reversed(expresion.split()):
        if not es_operador(token):
            pila.apilar(float(token))
        else:
            a = pila.desapilar()
            b = pila.desapilar()
            pila.apilar(aplicar_operador(token, a, b))
    
    return pila.desapilar()

# Ejemplos de uso
expresion_posfija = "3 4 + 2 *"
resultado_posfija = evaluar_posfija(expresion_posfija)
print(f"El resultado de la expresión posfija '{expresion_posfija}' es: {resultado_posfija}")

expresion_prefija = "* + 3 4 2"
resultado_prefija = evaluar_prefija(expresion_prefija)
print(f"El resultado de la expresión prefija '{expresion_prefija}' es: {resultado_prefija}")