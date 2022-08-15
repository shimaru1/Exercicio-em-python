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

    def exercicio5(self, eleitor, branco, nulos, validos, totalnulo, totalvalido, totalbranco):
        totalnulo = (nulos / eleitor) * 100
        totalvalido = (validos / eleitor) * 100
        totalbranco = (branco / eleitor) * 100
        return totalbranco, totalnulo, totalvalido, eleitor

    def exercicio6(self, salario, reajuste):
        return salario + (salario * reajuste / 100)

    def exercicio7(self, custo, distri, impos):
        distri = custo * (28 / 100)
        impos = custo * (45 / 100)

        return distri + impos + custo

    def exercicio8(self, nota1, nota2, nota3):
        return (nota1 + nota2 + nota3) / 3

    def exercicio9(self, maca):
        if maca >= 12:
            return maca * 1
        else:
            return maca * 1.3
        
    def exercicio10(self):
        return

    def exercicio11(self, bonus, venda, salario, comissao2, comissao):
        comissao2 = bonus * 5 / 100
        comissao = venda * 3 / 100
        return salario

    def exercicio12(self, saldo, credito, debito):
        return saldo + credito - debito

    def exercicio13(self, num):
        if num < 10 and num > 1:
            msg = ""
            for i in range(11):
                msg = msg + "\n{} * {} = {}".format(num, i, num * i)
            return msg
        else:
            print("Somente numero de 1 a 10")

    def exercicio14(self):
        return
