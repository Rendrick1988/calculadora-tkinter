import math
import os
from colorama import Fore, Style

class Calculadora:
   def __init__(self):
      self.historico =[]
      self.menu()

   def limpar_tela(self):
      os.system('cls'if os.name == 'nt'else 'clear')

   def somar(self,a,b):
      return a+b
   
   def subtrair(self,a,b):
      return a-b
   
   def multiplicar(self,a,b):
      return a*b
   
   def dividir(self,a,b):
      if b!=0:
         return a/b
      else:
         return"Erro:Divisão por zero!"
      
   def potencia(self, base, expoente):
        return math.pow(base, expoente)


   def raiz_quadrada(self,a):
      if a >=0:
         return math.sqrt(a)
      else:
         return f"Erro: Não é possivel calcular a raiz quadrada de um numero negativo."
      
   def mostrar_historico(self):
      print("\nHistórico de operações: ")
      if self.historico:
         for operacao in self.historico:
            print(Fore.YELLOW + operacao + Style.RESET_ALL)
      
      else:
         print(Fore.RED + "Nenhuma operação realizada ainda."+Style.RESET_ALL)

   def limpar_historico(self):
      self.historico.clear()
      print(Fore.RED + "Histórico limpo com sucesso!" + Style.RESET_ALL)


   def menu(self):
      while True:
         self.limpar_tela()
         print(Fore.CYAN + "====== Calculadora =====")
         print("\nEscolha uma operaçaõ:")
         print("1-Soma")
         print("2-Subtração")
         print("3-Multiplicação")
         print("4-Divisão")
         print("5-Potência")
         print("6-Raiz Quadrada")
         print("7-Mostrar Histórico")
         print("8-Limpar Histórico")
         print("9-Sair")

         try:
            opcao = int(input(Fore.GREEN +"\nDigite o numero da operação desejada: "))

            if opcao == 9:
               print(Fore.MAGENTA +"Encerrando Calculadora.Até logo!")
               break

            if opcao == 7:
               self.mostrar_historico()
               input("\nPressione Enter para continuar....")
               continue

            if opcao == 8:
               self.limpar_historico()
               input("\nPressione Enter para continuar....")
               continue

            if opcao in [1,2,3,4,5]:
               num1 = float(input(Fore.BLUE +"Digite o primeiro numero: "+Style.RESET_ALL))
               num2 = float(input(Fore.BLUE +"Digite o segundo numero: "+Style.RESET_ALL))
               if opcao == 1:
                  resultado = self.somar(num1,num2)
                  operacao = f"{num1} + {num2} = {resultado}"
               elif opcao == 2:
                  resultado = self.subtrair(num1,num2)
                  operacao = f"{num1} - {num2} = {resultado}"
               elif opcao == 3:
                  resultado = self.multiplicar(num1,num2)
                  operacao = f"{num1} * {num2} = {resultado}"
               elif opcao == 4:
                  resultado = self.dividir(num1,num2)
                  operacao = f"{num1} / {num2} = {resultado}"
               elif opcao == 5:
                  resultado = self.potencia(num1,num2)
                  operacao = f"{num1} ^ {num2} = {resultado}"
            elif opcao == 6:
               num1 = float(input(Fore.BLUE +"Digite o número: "+Style.RESET_ALL))
               resultado = self.raiz_quadrada(num1)
               operacao = f"√{num1} = {resultado}"
            else:
               print(Fore.RED + f"Opção invalida.Tente novamente.")
               input("\nPressione Enter para continuar....")
               continue
            print(Fore.YELLOW + f"Resultado:{resultado}" + Style.RESET_ALL)
            self.historico.append(operacao)
            input(f"Pressione Enter para continuar....")

         except ValueError:
            print(Fore.RED + "Entrada inválida. Por favor, digite números válidos." + Style.RESET_ALL)
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
   Calculadora()             



                     

            

            

      
   

   