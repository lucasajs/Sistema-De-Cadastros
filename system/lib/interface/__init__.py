def lerint(msg):
    while True:
        try:
            num= int(input(msg))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('ERRO! Digite um número inteiro válido')
            continue
        else:
            return num


def linha(tam= 40):
    return '-'*40


def cabeçalho(text):
    print(linha())
    print(text.center(40).upper())
    print(linha())


def menu(list):
    cabeçalho('menu principal')
    cont= 1
    for item in list:
        print(f'{cont} - {item}')
        cont += 1
    print(linha())
    opc= lerint('Sua opção: ')
    return opc
