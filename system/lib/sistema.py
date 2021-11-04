from system.lib.interface import *
from system.lib.arquivo import *

arq= 'cadastrados.txt'
if not arquivoExite(arq):
    criarArquivo(arq)


while True:
    opção= menu(['cadastrar nova pessoa','ver lista atual', 'sair do sistema'])
    if opção == 1:
        cabeçalho('novo cadastro')
        nome= str(input('Digite o nome: '))
        idade= lerint('Digite a idade: ')
        email= str(input('Digite o email: '))
        cadastro(arq, nome, idade, email)
    elif opção == 2:
        lerArquivo(arq)
    elif opção == 3:
        print('encerrando o sistema...')
        break