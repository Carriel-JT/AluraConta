class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo do titular {} é de {} reais".format(self.__titular, self.__saldo))

    def deposito(self, valor):
        self.__saldo += valor

    def __possibilidade_saque(self, valor_de_saque):
        valor_disponível_de_saque = self.__saldo + self.__limite
        return valor_de_saque <= valor_disponível_de_saque

    def saque(self, valor):
        if(self.__possibilidade_saque(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite