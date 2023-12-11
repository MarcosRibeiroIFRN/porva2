class Onibus:
    def __init__(self, linha):
        self.__linha = linha
        self.__motoristas = []

    def setLinha(self, linha):
        self.__linha = linha

    def editarLinha(self, linha):
        self.__linha = linha

    def getLinha(self):
        return self.__linha

    def getMotoristas(self):
        return self.__motoristas

    def vinculaMotorista(self,nome):
        self.__motoristas.append(nome)

    def __str__(self):
        return f"Linha: {self.__linha}; Motoristas: {self.__motoristas}"
