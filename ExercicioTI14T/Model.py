import math

class Model:

    def __init__(self):
        self.a = 0
        self.b = 0

    def exercicio1(self):
        a = 20
        b = 10
        self.a = b
        self.b = a
        a, b = b, a
        print(f'A={a} e B={b}')

    def exercicio2(self, num1):
        return num1 - 1

    def exercicio3(self, base, altura):
        return base * altura

    def exercicio4(self, ano, mes, dias):
        return ano * 360 + mes * 12 + dias

    def exercicio5(self, eleitor, branco, nulos, validos):
        return

    def exercicio6(self, salario, reajuste):
        return salario + (salario * reajuste / 100)








