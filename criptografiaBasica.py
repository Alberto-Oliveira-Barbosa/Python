import random


#criptografa o texto e gera uma chave
def criptografar():
    texto = getTexto()
    chave = getChave()
    codigo = str()
    # caso o usuário não passe um valor ele será gerado automaticamente
    if (chave == ''):
        chave = random.sample(range(100),1)
        chave = int(chave[0])
    # Faz a criptografia
    for i in range(len(texto)):
        codigo += chr(ord(texto[i]) + chave)
    return codigo, chave


# Revela o texto secreto
def descriptografar():
    codigo = getTexto()
    chave = 0
    while chave == 0 :
        chave = getChave()
        if(chave == ''):
            print('Voce precisa informar a chave de descriptografia\n\n')
            chave = 0
    texto = str()
    for i in range(len(codigo)):
        texto += chr(ord(codigo[i]) - chave)
    return texto

# Exibe as opções
def menu():
    print('\n')
    print('*' * 50)
    print('CRIPTOGRAFIA BÁSICA')
    print('*' * 50)
    print('Desenvolvido por Alberto Oliveira Barbosa.\n')

    print("Selecione uma opção \n1 - Criptografar um texto")
    print('2 - Descriptografar')
    print('3 - Sair\n')

# captura o Texto do usuário
def getTexto():
    return input('Digite o texto para criptografar/descriptografar\n\n')

# Captura a chave digitada pelo usuário
def getChave():
    while (True):
        op = input('Possui uma chave de compactação? S/N \n')

        if (op.upper()[0] == 'S'):
            chave = input('Digite a chave\n')
            if(not chave.isnumeric()):
                print('Chave com valor inválido!')
                continue
            else:
                return int(chave)
        elif (op.upper()[0] == 'N'):
            return ''
        else:
            print('Opção inválida')

# Valida a opção que o usuário digitou e valida ela.
def getOpcao():
    opcao = ''
    while(opcao == ''):
        opcao = input()

        if(opcao == '1'):
            return 1
        elif(opcao == '2'):
            return 2
        elif(opcao == '3'): exit()

        else:
            print("Opção inválida, Escolha 1, 2 ou 3\n")
            opcao = ''


# Loop principal do programa
while True:
    menu()
    op = getOpcao()

    if(op == 1):
        palavra_criptografada, chave = criptografar()
        print('O código gerado pelo programa é:\n' + palavra_criptografada)
        print('Sua chave de descriptografia é:\n' + str(chave) + '\n\n')

    else:
        palavra_descriptografada = descriptografar()
        print('Texto secreto: ' + palavra_descriptografada + '\n\n')
