import datetime
import textwrap

# ======== VARIÁVEIS ========
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

# ======== FUNÇÕES ========

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        hora = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        extrato += f"{hora} - Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(saldo, extrato, numero_saques):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        hora = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        extrato += f"{hora} - Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de, R${valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR${saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    usuario_existente = any(u['cpf'] == cpf for u in usuarios)
    if usuario_existente:
        print("Usuário já existe com esse CPF!")
        return usuarios

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })

    print(f"Usuário criado com sucesso! \n\t\tSeja Bem vindo(a) {nome} ao nosso banco ADS!")
    return usuarios

def criar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)

    if not usuario:
        print("Usuário não encontrado. Crie um usuário primeiro.")
        return contas

    numero_conta = len(contas) + 1
    contas.append({
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario
    })

    print(f"Conta criada com sucesso! Agência: 0001 Número: {numero_conta}")
    return contas

def listar_contas (contas):
    if not contas:
        print("Nenhuma conta foi criada ainda.")
        return

    for conta in contas:
        linha= f"""\
            Agencia:\t {conta['agencia']}
            C/C: \t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("= " * 100)
        print(textwrap.dedent(linha))

# ======== MENU E EXECUÇÃO ========
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar usuário
[c] Criar conta
[q] Sair
[lc]Listar Contas
=> """

while True:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "u":
        usuarios = criar_usuario(usuarios)

    elif opcao == "c":
        contas = criar_conta(contas, usuarios)

    elif opcao == "q":
        print("Sistema finalizado. Até logo!")
        break
        
    elif opcao == "lc":
        listar_contas

    else:
        print("Operação inválida. Por favor, tente novamente.")
