from system.lib.interface import *

def arquivoExite(nome):
    try:
        a= open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    a= open(nome, 'wt+')
    a.close()


def lerArquivo(nome):
    try:
        a= open(nome, 'rt')
    except:
        print('ERRO! não foi possível ler o arquivo')
    else:
        cabeçalho('LISTA DE CADASTROS')
        print(a.read())
    finally:
        a.close()


def cadastro(arq, nome='desconhecido', idade=0, email='não informado'):
    try:
        a= open(arq, 'at')
    except:
        print('ERRO! não foi possível abrir o arquivo.')
    else:
        a.write(f'{nome:<20} {idade:>3} anos\nEmail: {email}\n\n')
        print(f'{nome} cadastrado(a) com sucesso!')
        a.close()