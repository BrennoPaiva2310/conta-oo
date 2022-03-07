class Conta:
    def __init__(self, numero,titular,limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = 0
        self.__limite = 100

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite')

    def transferir(self, valor, conta):
        self.saca(valor)
        conta.deposita(valor)

    def get_extrato(self):
        print(f'O saldo do {self.__titular} é de R${self.__saldo}')

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

    @staticmethod
    def codigo_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
