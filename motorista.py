class Motorista:
    def __init__(self, nome):
        self.__nome = nome
        self.__onibus = []

    def setNome(self, nome):
        self.__nome = nome

    def editarNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def getOnibus(self):
        return self.__onibus

    def vinculaOnibus(self, onibus):
        self.__onibus.append(onibus)

    def removerOnibus(self, onibus):
        self.__onibus.remove(onibus)

    def __str__(self):
        return f"Nome: {self.get_nome()}; Ônibus: {self.__onibus}"
