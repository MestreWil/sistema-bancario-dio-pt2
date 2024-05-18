def menu():    
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Criar Usuario
    [ls] Listar Usuario
    [q] Sair
    
    => """
    return input(menu)
        
# o / siboliza que todos os argumentos passados devem seguir a ordem que foi estabelecida na função (por posição)
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.") 
    return saldo, extrato
    
    
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf, usuario):
    usuario_filtrados = [usuario for usuario in users if usuario['cpf'] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None
    
def criar_usuario(usuarios):
    cpf = input("Digite seu CPF (SOMENTE OS NÚMEROS): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('Esse CPF já está cadastrado!!!')
        return
    nome = input('Digite seu nome: ')
    data_nascimento = input("Informe sua data de nascimento: .")
    endereco = input("Digite seu endereço: ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Cadastro feito com SUCESSO!!!")

def listar_contas(contas):
    pass

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    users = list()
    contas = list()
    
    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "nu":
            criar_usuario(users)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, users)
            
            if conta: 
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)    

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
main()