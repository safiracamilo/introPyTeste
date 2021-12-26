# 1 - importação de pacotes
import json

# 2 - Classes

# 3 - Definições (Funções e Métodos)

dados = {}

dados['cliente'] = []  # indica a criação de um vetor, matriz, lista...
dados['cliente'].append({
    'nome': 'juca',
    'telefone': '119999999',
    'email': 'juca@iterasys.com.br'
})

def criar_json():
    with open(' clientes.json', 'w') as outfile:
        json.dump(dados,outfile)


def testar_criar_json():
    criar_json()
    print(dados['cliente'])


if __name__ == '__main__':
    testar_criar_json()


