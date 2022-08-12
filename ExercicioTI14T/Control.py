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
              "\n1. Exercicio: 1"                 +
              "\n2. Exercicio: 2"                 +
              "\n3. Exercicio: 3"                 +
              "\n4. Exercicio: 4"                 +
              "\n5. Exercicio: 5"                 +
              "\n6. Exercicio: 6"                 +
              "\n7. Exercicio: 7"                 +
              "\n8. Exercicio: 8"                 +
              "\n9. Exercicio: 9")
        self.setOpcao(int(input())) #Coletando a escolha do usuário

    def operacao(self):
        while(self.getOpcao != 0):
            self.menu()