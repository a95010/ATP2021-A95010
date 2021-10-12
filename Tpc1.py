import random

def jogador_comeca (resultado):
    while (resultado > 0):
        a = int (input("insira um numero de 1 a 4: "))
        resultado = resultado - a
        print (resultado)
        if (resultado > 5):
            b = 5 - a
            resultado = resultado - b
            print (resultado)
        else:
            if (resultado != 0):
                resultado = resultado - resultado + 1
                print (resultado)
                continue
            else:
                print ("O computador ganhou!")

def computador_comeca (resultado):
    controlo = True
    while (resultado > 0):
        j = 0
        c = 0
        if (controlo == True):
            c = random.randint (1,4)
            resultado = resultado - c
            print (resultado)
            controlo = False
        j = int (input("Escolha um número de 1 a 4: "))
        resultado = resultado - j
        print (resultado)
        if (resultado == 1):
            print ("Parabens, ganhou o jogo!")
            break
        if (j + c == 5):
            controlo = True
            continue
        else:
            if (j + c < 5):
                if (c != 0):
                    c = 5 - (c + j)
                    resultado = resultado - c
                    print (resultado)
                else:
                    c = 5 - j
                    resultado = resultado - c
                    print (resultado)
                if (resultado == 1):
                    print ("O computador ganhou!")
                    break 
            else:
                c = 10 - j - c
                resultado = resultado - c
                print (resultado)


def main():
    resultado = 21
    print (" Menu: \n 1-Começa o jogador \n 2-Começa o computador \n ")
    numero = int (input( "Escolha uma opção: "))

    if (numero == 1):
        jogador_comeca (resultado)
    else:
        computador_comeca (resultado)

if __name__ == "__main__":
    main ()
