#importação:
from CLass_calculator import Calculadora

#declarando variaveis:
pergunta1 = "n"

#estruturas de repetição:
while pergunta1 == "nao" or pergunta1 == "n" or pergunta1 == "não":
    pergunta = "sim"
    tc = str(input("Você deseja calcular ou fazer uma tabuada ?\n(Escreva:tabuada ou calcular)\n."))
    while not(tc == "tabuada" or tc == "calcular"):
        tc = str(input("O valor escrito n é valido por favor digite novamente\n."))


    if tc == "calcular":
        print("Calculadora\n")
        while pergunta == "sim" or pergunta == "s":
            
            #variaveis internas:
            n1=int(input("Escreva um numero inteiro:\n."))
            n2=int(input("Escreva mais um numero inteiro:\n."))
            q=str(input("Você deseja multiplicar, dividir, somar ou subtrair esses valores?\n."))

            calculadora=Calculadora(n1,n2)
            
            #estrutura de repetição interna
            while not(q == "somar" or q == "multiplicar"  or q == "dividir" or q == "subtrair" or q == "+" or q == "-" or q == "/" or q == "x" or q == "*"):
                q =input("Voce escreveu um valor incompativel, por favor digite novemente:\n.")

            
            
            #o programa:

            if q == "somar" or q == "+":
                print ("{} + {} = {}\nObrigado!".format(n1, n2, calculadora.soma()))
            elif q == "subtrair" or q == "-":
                print ("{} - {} = {}\nObrigado!".format(n1, n2, calculadora.subtracao()))
            elif q == "multiplicar" or q == "x" or q == "*":
                print ("{} x {} = {}\nObrigado!".format(n1, n2, calculadora.multiplicacao()))
            else:
                print ("{} / {} = {}\nObrigado!".format(n1, n2, calculadora.divisao()))
            
            #finalização do programa:
            pergunta=input("\nVoce deseja continuar calculando ?\n.")
    elif tc == "tabuada":
        print("Tabuadas:")
        while pergunta == "sim" or pergunta == "s":
            #variaveis internas:
            n1=int(input("escreva um numero inteiro:\n"))

            #o programa
            print("\nObrigado\nA tabuada completa desse numero é:\n")
            for x in range(11):
                calculadora = Calculadora(n1, x)
                print("{} x {} = {}".format(n1, x, calculadora.multiplicacao()))
            
            #pergunta de finalização
            pergunta= input("\nDeseja fazer outra tabuada ?\n (digite: sim ou nao)\n")
    #final do programa:
    pergunta1=input("fechar o programa ?\n.")
print("Obrigado!\nFim do programa")