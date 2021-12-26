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
    print_hi('Safira')

    resultado = calcular_area_do_retangulo(3,4)
    print (f'A area do retangulo é de {resultado} m')

    resultado = calcular_area_do_quadrado(5)
    print(f'A area do quadrado é de {resultado} m')


    resultado = calcular_area_do_triangulo(6,7)
    print(f'A area do triangulo é de {resultado} m')

    #executar a contagem progessiva
    contagem_progessiva(11)

    apoiar_canditato('kaise',99)

    # brincar de plim
    brincar_de_plim(100)