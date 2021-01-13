#criando classes
class Calculadora:
    def __init__(self, valor1, valor2):
        self.a = valor1
        self.b = valor2
    def soma (self):
        return self.a + self.b
    def subtracao (self):
        return self.a - self.b
    def divisao (self):
        return self.a / self.b
    def multiplicacao (self):
        return self.a * self.b