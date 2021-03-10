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

    def saque(self, valor):
        self.__saldo -= valor

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    def retorna_saldo(self):
        return self.__saldo

    def retorna_titular(self):
        return self.__titular

    def retorna_limite(self):
        return self.__limite
    