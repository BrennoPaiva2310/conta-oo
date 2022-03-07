class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    #Getters
    @property
    def nome(self):
        print('Ola')
        return self.__nome.title()

    #Setters
    @nome.setter
    def nome(self, nome):
        if len(nome)>=5:
            self.__nome = nome
        else:
            print('Nome invalido')


