from motorista import Motorista
from onibus import Onibus
import time

  
class Interface:

  def __init__(self):
    self.__motoristas = []
    self.__onibus = []
      
  def menu(self):
      print("Bem vindo ao sistema da frota Trampolim da Vitória\n")
      print("Escolha entre uma das opções abaixo:")
      opcao = int(input("1 - Cadastrar\n2 - Editar\n3 - Listar\n4 - Vincular\n0 - Encerrar\n"))

      if opcao == 1:
          opcao2 = int(input("Menu de cadastro\nEscolha uma opção:\n1 - Cadastrar ônibus\n2 - Cadastrar Motorista\n0 - Voltar ao menu principal\n"))

          if opcao2 == 1:
              linha = int(input("Digite o número da linha do Ônibus: "))
              cadastro = Onibus(linha)
              self.__onibus.append(cadastro)
              print(f"{linha} cadastrada com sucesso!")

          elif opcao2 == 2:
              nome = input("Digite o nome do Motorista: ")
              cadastro = Motorista(nome)
              self.__motoristas.append(cadastro)
              print(f"{nome} cadastrado com sucesso!")
              print("Retornando ao menu inicial\n\n\n")
              time.sleep(3)

          elif opcao2 == 0:
              self.menu()

          else:
              print("Opção inválida, tente novamente")
              self.menu()

      elif opcao == 2:
          opcao2 = int(input("Menu de edição, escolha a opção:\n1 - Editar motorista\n2 - Editar ônibus\n0 - Voltar menu principal\n"))

          if opcao2 == 1:
              nome = input("Digite o nome do motorista que deseja editar: ")
              novoNome = input("Digite o novo nome do motorista: ")
              self.editarMotorista(nome, novoNome)

          elif opcao2 == 2:
              linha = input("Digite o número da linha do Ônibus que deseja editar: ")
              novaLinha = input("Digite a nova linha do ônibus: ")
              self.editarOnibus(linha, novaLinha)

          elif opcao2 == 0:
              print("Voltando ao menu principal")
              self.menu()

          else:
              print("Opção inválida, tente novamente")
              self.menu()

      elif opcao == 3:
          opcao2 = int(input("Menu de listagem, escolha a opção:\n"
                            "1 - Listar motoristas\n"
                            "2 - Listar ônibus\n"
                            "3 - Listar motoristas por ônibus\n"
                            "4 - Listar ônibus por motorista\n"
                            "0 - Voltar menu principal\n"))

          if opcao2 == 1:
              print("\n" * 130)
              print("\n\n\nMotoristas da trampolim:\n")
              for motorista in self.__motoristas:
                  print(motorista.getNome()+"\n")
              print("Retornando ao menu inicial")
              time.sleep(3)
                  

          elif opcao2 == 2:
              for onibus in self.__onibus:
                  print(onibus.getLinha())

          elif opcao2 == 3:
              linha = int(input("Digite o número da linha que você deseja listar: "))
              for onibus in self.__onibus:
                  if onibus.getLinha() == linha:
                      print(onibus.getMotoristas())

                  else:
                      print("Linha não encontrada")
              self.menu()

          elif opcao2 == 4:
              nome = input("Digite o nome do motorista que deseja listar: ")
              for motorista in self.__motoristas:
                  if motorista.getNome() == nome:
                      print(motorista.getOnibus())
                  else:
                      print("Motorista não encontrado")
                      self.menu()

          elif opcao2 == 0:
              self.menu()

          else:
              print("Opção inválida, tente novamente")
              self.menu()

      elif opcao == 4:
          opcao2 = int(input("Menu de vinculação, escolha a opção:\n"
                            "1 - Vincular motorista a ônibus\n"
                            "2 - Vincular ônibus a motorista\n"
                            "0 - Voltar menu principal\n"))

          if opcao2 == 1:
              nome = input("Digite o nome do motorista que deseja vincular: ")
              linha = int(input("Digite o número da linha do Ônibus que deseja vincular: "))
              self.vincularMotoristaOnibus(nome, linha)

          elif opcao2 == 2:
              linha = int(input("Digite o número da linha do Ônibus que deseja vincular: "))
              nome = input("Digite o nome do motorista que deseja vincular: ")
              self.vincularOnibusMotorista(linha, nome)

          elif opcao2 == 0:
              print("Voltando ao menu principal")
              self.menu()

      elif opcao == 0:
          print("Encerrando o sistema")

      else:
          print("Opção inválida, tente novamente")

      # Chama a função menu novamente se a opção não for 0
      if opcao != 0:
          self.menu()
    
  def adicionarMotorista(self, nome):
    self.__motoristas.append(Motorista(nome))

  def adicionarOnibus(self, linha):
    self.__onibus.append(Onibus(linha))

  def editarMotorista(self, nome, novo_nome):
    for motorista in self.__motoristas:
      if motorista.getNome() == nome:
        motorista.editarNome(novo_nome)

  def editarOnibus(self, linha, nova_linha):
    for onibus in self.__onibus:
      if onibus.__linha == linha:
        onibus.editarLinha(nova_linha)

  def vincularMotoristaOnibus(self, nome, linha):
    for motorista in self.__motoristas:
      if motorista.getNome() == nome:
        for onibus in self.__onibus:
          if onibus.getLinha() == linha:
            if onibus.getLinha() not in motorista.getOnibus():
              motorista.vinculaOnibus(onibus.getLinha())
              onibus.vinculaMotorista(motorista.getNome())
            
              print("Motorista cadastrado com sucesso")
            else:
              print("Motorista já cadastrado")
          else: 
            print("Linha inexistente")
      else:
        print("Motorista inexistente")
  def vincularOnibusMotorista(self, linha, nome):
    for onibus in self.__onibus:
      if onibus.getLinha() == linha:
        for motorista in self.__motoristas:
          if motorista.getNome() == nome:
            if nome not in onibus.getMotoristas():
              motorista.vinculaOnibus(linha)
              onibus.vinculaMotorista(nome)
            
              print("Onibus cadastrado com sucesso")
              break
            else:
              print("Motorista já cadastrado")
          else: 
            print("Motorista inexistente")
      else:
        print("Onibus inexistente")


  def desvincularMotoristaOnibus(self, nome, linha):
    for motorista in self.__motoristas:
      if motorista.getNome()== nome:
        for onibus in self.__onibus:
          if onibus.getLinha()== linha:
            if onibus not in motorista.__onibus:
              motorista.removerOnibus(onibus)
              print("Motorista cadastrado com sucesso")
            else:
              print("Motorista já cadastrado")
          else: 
            print("Linha inexistente")
      else:
        print("Motorista inexistente")
  
  def __str__(self):
    print("Motoristas:")
    for motorista in self.__motoristas:
      print(motorista)
    print("Onibus:")
    for onibus in self.__onibus:
      print(onibus)
      