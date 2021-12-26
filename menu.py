def print_hi(name):

    print(f'Oi, {name}')

def calcular_area_do_retangulo(largura,comprimento):
    return  largura * comprimento

def calcular_area_do_quadrado(lado):
    return  lado **2

def calcular_area_do_triangulo(base, altura):
    return  base * altura / 2

def contagem_progessiva(fim):
    for numero in range (fim): #repetir o bloco de zero até o fim
        print(numero) # exibir o número


def apoiar_canditato(nome, vezes):
    for numero in range (vezes):
        #contador = numero + 1
        #print(f'{contador} - {nome}')

        if numero < 9:
           print(f'0{numero + 1} - {nome}')
        else:
           print(numero +1, '-', nome)

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>9}'.format(numero))

#estrutura de identificacao / execucao sprint
if __name__ == '__main__':

    resposta = "C"

    while resposta.upper() != 'Z':

        print('###############################')
        print('#                             #')
        print('## MENU DE OPÇÕES            #' )
        print('#                             #')
        print('# 1 - Olá mundo               #')
        print('# 2 - Área do retângulo       #')
        print('# 3 - Área do quadrado        #')
        print('# 4 - Área do trinângulo      #')
        print('# 5 - Contagem Regressiva     #')
        print('# 6 - Apoiar candidato        #')
        print('# 7 - Brincar de Plim         #')
        print('#                             #')
        print('# Z - sair                    #')
        print('#                             #')
        print('###############################')

        resposta = input('escolha sua opcao')
        print(f'A sua escolha foi:  {resposta}')

        if resposta.upper() != 'Z':
            if resposta == '1':
                print_hi('Safira')
            elif resposta == '2':
                resultado = calcular_area_do_retangulo(8,7)
                print (f' A área do retângulo é de:{resultado} m')
            elif resposta == '3':
                resultado = calcular_area_do_quadrado(6)
                print(f' A área do quadrado é de:{resultado} m')
            elif resposta == '4':
                resultado = calcular_area_do_triangulo(5,8)
                print(f' A área do triangulo é de:{resultado} m')
            elif resposta == '5':
                contagem_progessiva(10)
            elif resposta == '6':
                apoiar_canditato('Murphy',13)
            elif resposta == '7':
                brincar_de_plim(7)
            else:
                print('Você digitou um a opção invalida. Escolha uma opção de 1 a 7 ')
        else:

            print ("Você escolheu sair. Volte sempre")


