import os #import da biblioteca para comandos de arquivo no sistema
from datetime import datetime #import da função de data e hora pedido no extrato
dataehora = datetime.now() #defindo a variável para horário atual
dataehoraemtexto = dataehora.strftime("%Y-%m-%d %H:%M") #formatando a variavel de horario atual

def criarConta(): #criação da função de criação de conta
    nome = input("Digite o seu nome: ") #solicitação do nome ao usuário
    CPF = input("Digite o seu CPF: ") #solicitação do CPF ao usuário
    senha = input("Digite a sua senha: ") #solicitação de senha ao usuário
    saldo = float(input("Digite o valor incial: ")) #solicitação de um valor incial para a conta ao usuário
    print("1 - Conta Salário: 5% de taxa a cada débito + não permite saldo negativo") #apresenta a 1 opção de conta
    print("2 - Conta Comum: 3% de taxa a cada débito + permite saldo negativo até 500") #apresenta a 2 opção de conta
    print("3 - Conta Plus: 1% de taxa a cada débito + permite saldo negativo até 5000") #apresenta a 1 opção de conta
    conta = input("Escolha o tipo da conta: ") #solitação de escolha de conta ao usuário
    if os.path.isfile(CPF+".txt"): #condição de verificação do arquivo pelo CPF que é o nome do arq txt
        print("Cliente já cadastrado") #aviso de  cadastro ja feito
    else: #condição para o que sobra, ou seja, CPF não ter sido cadastrado anteriormente
        arquivo = open(CPF+".txt", "w") #criação de um arquivo utilizando o CPF inserido pelo usuário
        arquivo.write("%s\n" % nome) #armazenamento do nome no arquivo .txt
        arquivo.write("%s\n" % CPF) #armazenamento do CPF no arquivo .txt
        arquivo.write("%s\n" % senha) #armazenamento do senha no arquivo .txt
        arquivo.write("%s\n" % conta) #armazenamento do conta no arquivo .txt
        arquivo.write("%s\n" % "Data:") #formatação para o extrato
        arquivo.write("%s\n" % dataehoraemtexto,) #formatação para o extrato
        arquivo.write("%s\n" % " ") #formatação para o extrato
        arquivo.write("%s\n" % "+") #formatação para o extrato
        arquivo.write("%s\n" % " ") #formatação para o extrato
        arquivo.write("%s\n" % saldo) #armazenamento do do valor inicial inserido no arquivo .txt (formatação do extrato)
        arquivo.write("%s\n" % " ") #formatação para o extrato
        arquivo.write("%s\n" % "Tarifa:") #formatação para o extrato
        arquivo.write("%s\n" % "0.00") #formatação para o extrato
        arquivo.write("%s\n" % " ") #formatação para o extrato
        arquivo.write("%s\n" % "Saldo:") #formatação para o extrato
        arquivo.write("%s\n" % saldo) #armazenamento do do valor inicial inserido no arquivo .txt
        arquivo.close() #fechamento do arquvio
        print("Cadastro Concluído") #aviso de cadastro concluido

def deletarConta(): #criação da função para deletar a conta
    CPF = input("Digite o seu CPF: ") #solicitação do CPF ao usuário
    if os.path.isfile(CPF+".txt"): #condição de verificação do arquivo pelo CPF que é o nome do arq txt
        os.remove(CPF+".txt") #comando importado para deletar o arquivo
        print("Conta Excluida") #aviso de conta concluída
    else: #condição para se o CPF não tiver sido cadastro ou estiver incorreto
        print("Informação Incorreta ou Conta Inexistente") #aviso de falha no processo de delete

def sacarDinheiro(): #criação da função de saque
    CPF = input("Digite o seu CPF: ") #solicitação do CPF ao usuário
    senha = input("Digite a sua senha: ") #solicitação da senha ao usuário
    saque = float(input("Digite o valor de saque: ")) #solicitação do valor de saque ao usuário
    tarifa1 = float((5/100)*saque) #tafira que será cobrada no saque se a conta for tipo salário
    tarifa2 = float((3/100)*saque) #tafira que será cobrado se a conta for tipo comum
    tarifa3 = float((1/100)*saque) #tafira que será cobrado se a conta for tipo plus
    key = [] #criação da váriavel key
    if os.path.isfile(CPF+".txt"): #condição de verificação do arquivo pelo CPF que é o nome do arq txt
        arquivo = open(CPF+".txt", "r") #comando para abrir o arquivo para ler
        for lista in arquivo.readlines(): #
            key.append(lista.strip())     #indica que toda a informação escrita sera adicionada com append
        arquivo.close() #fecha o arquivo
        if senha == key[2]: #condição para validação da senha inserida pela usuário da escrita no .txt
            if "1" == key[3]: #condição para validação para avaliar qual tarifa sera utilizada na cobrança adicional do saque
                if saque > float(key[-1]): #condição para não permitir saldo negativo relativo ao tipo de conta salário
                    print("Saldo Insuficiente") #aviso de saldo insuficiente caso saque > saldo
                else:  #condição caso o saque não deixe a conta com saldo negativo
                    arquivo = open(CPF+".txt", "a") #abrir arquivo para update
                    arquivo.write("%s\n" % "Data:") #formatação para extrato
                    arquivo.write("%s\n" % dataehoraemtexto) #formatação para extrato data e hora importados da biblioteca
                    arquivo.write("%s\n" % " ") #formatação para extrato
                    arquivo.write("%s\n" % "-") #formatação para extrato sinal de negativo representando o débito
                    arquivo.write("%s\n" % " ") #formatação para extrato
                    arquivo.write("%s\n" % saque) #formatação para extrato valor retirado
                    arquivo.write("%s\n" % " ") #formatação para extrato
                    arquivo.write("%s\n" % "Tarifa:") #formatação para extrato 
                    arquivo.write("%s\n" % tarifa1) #formatação para extrato valor tarifado do saque
                    arquivo.write("%s\n" % " ") #formatação para extrato
                    arquivo.write("%s\n" % "Saldo:") #formatação para extrato
                    arquivo.write("%s\n" % (float(key[-1])-(saque+tarifa1))) #saldo da conta
                    arquivo.close() #fechamento do arquivo
                    print("Saque Concluído com Sucesso") #aviso de saque concluido
            elif "2" == key[3]: #condição para validação para avaliar qual tarifa sera utilizada na cobrança adicional do saque
                if saque == (float(key[-1]) + 501): #condição para permitir um credito negativo de até 500, relativo ao tipo de conta comum
                    print("Saldo Insuficiente") #aviso de saldo insuficiente caso saque = saldo +501
                else:    #condição caso o saque não deixe a conta com saldo negativo
                    arquivo = open(CPF+".txt", "a") #abrir arquivo para update
                    arquivo.write("%s\n" % " ") #formatação para extrato
                    arquivo.write("%s\n" % "Data:") #formatação para extrato
                    arquivo.write("%s\n" % dataehoraemtexto) #formatação para extrato data e hora importados da biblioteca
                    arquivo.write("%s\n" % " ") #formatação para extrato
                    arquivo.write("%s\n" % "-") #formatação para extrato sinal de negativo representando o débito
                    arquivo.write("%s\n" % " ") #formatação para extrato
                    arquivo.write("%s\n" % saque) #formatação para extrato valor retirado
                    arquivo.write("%s\n" % " ") #formatação para extrato
                    arquivo.write("%s\n" % "Tarifa:") #formatação para extrato
                    arquivo.write("%s\n" % tarifa2) #formatação para extrato valor tarifado do saque
                    arquivo.write("%s\n" % " ") #formatação para extrato
                    arquivo.write("%s\n" % "Saldo:") #formatação para extrato
                    arquivo.write("%s\n" % (float(key[-1])-(saque+tarifa2))) #saldo da conta
                    arquivo.close() #fechamento do arquivo
                    print("Saque Concluído com Sucesso") #aviso de saque concluido
            elif "3" == key[3]: #condição para validação para avaliar qual tarifa sera utilizada na cobrança adicional do saque
                if saque == (float(key[-1]) + 5001): #condição para permitir um credito negativo de até 5000, relativo ao tipo de conta plus
                    print("Saldo Insuficiente") #aviso de saldo insuficiente caso saque = saldo +5001
                else:    #condição caso o saque não deixe a conta com saldo negativo
                    arquivo = open(CPF+".txt", "a") #abrir arquivo para update
                    arquivo.write("%s\n" % " ") #formatação para extrato
                    arquivo.write("%s\n" % "Data:") #formatação para extrato
                    arquivo.write("%s\n" % dataehoraemtexto) #formatação para extrato data e hora importados da biblioteca
                    arquivo.write("%s\n" % " ") #formatação para extrato
                    arquivo.write("%s\n" % "-") #formatação para extrato sinal de negativo representando o débito
                    arquivo.write("%s\n" % " ") #formatação para extrato
                    arquivo.write("%s\n" % saque) #formatação para extrato valor retirado
                    arquivo.write("%s\n" % " ") #formatação para extrato
                    arquivo.write("%s\n" % "Tarifa:") #formatação para extrato
                    arquivo.write("%s\n" % tarifa3) #formatação para extrato valor tarifado do saque
                    arquivo.write("%s\n" % " ") #formatação para extrato
                    arquivo.write("%s\n" % "Saldo:") #formatação para extrato
                    arquivo.write("%s\n" % (float(key[-1])-(saque+tarifa3))) #saldo da conta
                    arquivo.close() #fechamento do arquivo
                    print("Saque Concluído com Sucesso")   #aviso de saque concluido     
        else: #condição para se o CPF e Senha não forem iguais
            print("Credencial Invalida") #aviso de credencial inválida
             
def depositarDinheiro(): #criação da função de débito
    CPF = input("Digite o seu CPF: ") #solicitação do CPF ao usuário
    senha = input("Digite a sua senha: ") #solicitação da senha ao usuário
    deposito = float(input("Digite o valor de depósito: ")) #solicitação do valor de saque ao usuário
    key = [] #criação da váriavel key
    if os.path.isfile(CPF+".txt"): #condição de verificação do arquivo pelo CPF que é o nome do arq txt
        arquivo = open(CPF+".txt", "r") #comando para abrir o arquivo para ler
        for lista in arquivo.readlines(): #
            key.append(lista.strip())     #indica que toda a informação escrita sera adicionada com append
        arquivo.close() #fechamento do arquivo
        if senha == key[2]: #condição para validação da senha inserida pela usuário da escrita no .txt
            arquivo = open(CPF+".txt", "a") #abrir arquivo para update
            arquivo.write("%s\n" % "Data:") #formatação para extrato
            arquivo.write("%s\n" % dataehoraemtexto) #formatação para extrato data e hora importados da biblioteca
            arquivo.write("%s\n" % " ") #formatação para extrato
            arquivo.write("%s\n" % "+") #formatação para extrato
            arquivo.write("%s\n" % " ") #formatação para extrato
            arquivo.write("%s\n" % deposito) #formatação para extrato valor depositado
            arquivo.write("%s\n" % "Tarifa:") #formatação para extrato
            arquivo.write("%s\n" % "0.00") #formatação para extrato
            arquivo.write("%s\n" % " ") #formatação para extrato
            arquivo.write("%s\n" % "Saldo:") #formatação para extrato
            arquivo.write("%s\n" % (float(key[-1])+deposito)) #saldo da conta
            arquivo.close() #fechamento do arquivo
            print("Deposito Concluído com Sucesso") #aviso de deposito concluido
        else: #condição para se a senha não for igual
            print("Credencial Invalida") #aviso de credenvial invalida

def verSaldo(): #criação da função para ver o saldo
    CPF = input("Digite o seu CPF: ") #solicitação do CPF ao usuário
    senha = input("Digite a sua senha: ") #solicitação da senha ao usuário
    key = [] #criação da váriavel key
    if os.path.isfile(CPF+".txt"):  #condição de verificação do arquivo pelo CPF que é o nome do arq txt
        arquivo = open(CPF+".txt", "r") #abrir o arquiv para ler
        for lista in arquivo.readlines(): #
            key.append(lista.strip()) #indica que toda a informação escrita sera adicionada com append
        arquivo.close() #fechamento do arquivo
        if senha == key[2]: #condição para validação da senha inserida pela usuário da escrita no .txt
            arquivo = open(CPF+".txt", "r") #abrir o arquiv para ler
            print(key[-1]) #mostra o saldo para o usuário
            arquivo.close() #fechamento do arquivo
            print("|||||| SALDO ||||||") #formatação de aviso do saldo
        else: #condição para se a senha não for igual
             print("Credencial Invalida")  #aviso de credencial invalida 

def verExtrato(): #criação da função para ver o saldo
    CPF = input("Digite o seu CPF: ") #solicitação do CPF ao usuário
    senha = input("Digite a sua senha: ") #solicitação da senha ao usuário
    key = [] #criação da váriavel key
    if os.path.isfile(CPF+".txt"): #condição de verificação do arquivo pelo CPF que é o nome do arq txt
        arquivo = open(CPF+".txt", "r") #abrir o arquiv para ler
        for lista in arquivo.readlines(): #
            key.append(lista.strip()) #indica que toda a informação escrita sera adicionada com append
        arquivo.close() #fechamento do arquivo
        if senha == key[2]:  #condição para validação da senha inserida pela usuário da escrita no .txt
            arquivo = open(CPF+".txt", "r") #abrir o arquiv para ler
            print(*key[0:3], sep="\n") #escrever o nome,cpf,senha e tipo da conta um em baixo do outro
            print(*key[4:])
            arquivo.close() #fechamento do arquivo
            print("|||||| EXTRATO ||||||") #aviso do extrato
    else: #condição para se a senha não for igual
        print("Credencial Invalida") #aviso de credencial invalida 
                               
def menu(): #criação da função de menu
    while True: #mantém o menu em loop
        print("="*30) #formatação 
        print("{:^30}".format("QuemPoupaTem")) #formatação
        print("="*30) #formatação
        print("|||||| Menu ||||||")  #escrever Menu com uma formatação
        print("1 - Criar Nova Conta") #mostrar opção 1
        print("2 - Deletar Conta") #mostrar opção 2
        print("3 - Sacar dinheiro") #mostrar opção 3
        print("4 - Depositar") #mostrar opção 4
        print("5 - Saldo")   #mostrar opção 5
        print("6 - Extrato")  #mostrar opção 6
        print() #formatação
        print("0 - Sair do Menu") #mostrar opção 0

        opcao = input("Escolha uma das operações: ") #solitação para o usuário escolher uma operação
        if opcao == "1": #condição para se usuário escolher a opção 1
            criarConta() #chama a função de criação de conta
        elif opcao == "2": #condição para se usuário escolher a opção 2
            deletarConta() #chama a função de deletar a conta
        elif opcao == "3": #condição para se usuário escolher a opção 3
            sacarDinheiro() #chama a fução para sacar o dinheir
        elif opcao == "4": #condição para se usuário escolher a opção 4
            depositarDinheiro() #chama a função para depositar o dinheiro
        elif opcao == "5": #condição para se usuário escolher a opção 5
            verSaldo() #chama a função para ver o saldo
        elif opcao == "6": #condição para se usuário escolher a opção 6
            verExtrato() #chama a função para ver extrato
        elif opcao == "0": #condição para se usuário escolher a opção 0
            break  #para o looping do menu

menu()           