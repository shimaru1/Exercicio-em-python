from Model import Model

class Control:
    def __init__(self):
        self.opcao = -1
        self.num1  = 0
        self.num2  = 0
        self.modelo = Model() #Conectando com a classe model

    def getNum1(self):
        return self.num1

    def getNum2(self):
        return self.num2

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def setNum1(self, num1):
        self.num1 = num1

    def setNum2(self, num2):
        self.num2 = num2

    def coletar(self):
        print("Informe um número: ")
        self.setNum1(float(input()))

        print("Informe outro número: ")
        self.setNum2(float(input()))

    def menu(self):
        print("\nEscolha uma das opções abaixo: " +
              "\n0. Sair"                         +
              "\n1. Exercicio 1"                  +
              "\n2. Exercicio 2"                  +
              "\n3. Exercicio 3"                  +
              "\n4. Exercicio 4"                  +
              "\n5. Exercicio 5"                  +
              "\n6. Exercicio 6"                  +
              "\n7. Exercicio 7"                  +
              "\n8. Exercicio 8"                  +
              "\n9. Exercicio 9"                  +
              "\n10. Exercicio 10"                +
              "\n11. Exercicio 11"                +
              "\n12. Exercicio 12"                +
              "\n13. Exercicio 13"                +
              "\n14. Exercicio 14"                +
              "\n15. Exercicio 15"                +
              "\n16. Exercicio 16"                +
              "\n17. Exercicio 17"                +
              "\n18. Exercicio 18"                +
              "\n19. Exercicio 19"                +
              "\n20. Exercicio 20")
        self.setOpcao(int(input())) #Coletando a escolha do usuário

    def operacao(self):
        while self.opcao != 0:
            self.menu()
        if self.opcao == 1:
            self.Model.exercicio1()
        elif self.opcao == 2:
            print("informe um numero")
            self.setNum1(float(input()))
            print("O antecessor do número é: {}".format(self.Model.exercicio2(self.getNum1())))
        elif self.opcao == 3:
            print("informe a base:")
            self.setNum1(float(input()))
            print("informe a altura:")
            self.setNum2(float(input()))
            print("A area do retangulo e: {}" .format(self.Model.exercicio3(self.getNum1(), self.getNum2())))
        elif self.opcao == 4:
            print("informe o anos:")
            self.setNum2(float(input()))
            print("informe o meses:")
            self.setNum3(float(input()))
            print("informe o dias:")
            self.setNum4(float(input()))
            print("Sua idade em dias é: {}".format(self.Model.exercicio4(self.getNum2(), self.getNum3(), self.getNum4())))
        elif self.opcao == 6:
            print("informe o salario")
            self.setNum1(float(input()))
            print("informe o reajuste")
            self.setNum2(float(input()))
            print("O valor do novo salario é: {}".format(self.Model.exercicio6(self.getNum1(), self.getNum2())))
        elif self.Opcao() == 13:
                print("Informe um número: ")
                print(self.modelo.exercicio13(float(input())))
        else:
            print("Obrigado!")