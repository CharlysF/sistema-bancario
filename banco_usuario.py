# Dicionário para armazenar usuários e suas contas
usuarios = {}
contas = {}

def criar_usuario(nome_usuario):
    """Cria um novo usuário com um nome de usuário único."""
    if nome_usuario in usuarios:
        print("Usuário já existe.")
    else:
        usuarios[nome_usuario] = {"nome": nome_usuario}
        contas[nome_usuario] = {
            "saldo": 0,
            "limite": 1000,
            "extrato": "",
            "numero_saque": 0,
            "limite_saque": 5
        }
        print(f"Usuário {nome_usuario} criado com sucesso.")

def criar_conta_corrente(nome_usuario):
    """Cria uma conta corrente para o usuário existente."""
    if nome_usuario not in usuarios:
        print("Usuário não encontrado. Crie um usuário primeiro.")
    elif nome_usuario in contas:
        print("Conta corrente já existe para este usuário.")
    else:
        contas[nome_usuario] = {
            "saldo": 0,
            "limite": 1000,
            "extrato": "",
            "numero_saque": 0,
            "limite_saque": 5
        }
        print(f"Conta corrente criada para o usuário {nome_usuario}.")

def depositar(nome_usuario, valor):
    """Deposita um valor na conta do usuário."""
    if nome_usuario not in contas:
        print("Conta não encontrada.")
    elif valor <= 0:
        print("Valor inválido para depósito.")
    else:
        contas[nome_usuario]["saldo"] += valor
        contas[nome_usuario]["extrato"] += f'Depósito: R$ {valor:.2f}\n'
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

def sacar(nome_usuario, valor):
    """Saca um valor da conta do usuário."""
    conta = contas.get(nome_usuario)
    
    if not conta:
        print("Conta não encontrada.")
        return
    
    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > conta["limite"]
    excedeu_saques = conta["numero_saque"] >= conta["limite_saque"]
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor <= 0:
        print("Operação falhou! Valor informado é inválido.")
    else:
        conta["saldo"] -= valor
        conta["extrato"] += f'Saque: R$ {valor:.2f}\n'
        conta["numero_saque"] += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def extrato(nome_usuario):
    """Exibe o extrato e o saldo da conta do usuário."""
    conta = contas.get(nome_usuario)
    
    if not conta:
        print("Conta não encontrada.")
        return
    
    print("\n==================== EXTRATO ====================")
    print("Não foram realizadas movimentações." if not conta["extrato"] else conta["extrato"])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("====================")

def credito(nome_usuario):
    """Disponibiliza crédito baseado no saldo do usuário."""
    conta = contas.get(nome_usuario)
    
    if not conta:
        print("Conta não encontrada.")
        return
    
    if conta["saldo"] >= 1000:
        credito_disponivel = conta["saldo"] * 0.25
        print(f"Crédito disponível: R$ {credito_disponivel:.2f}")
    else:
        print("Saldo insuficiente para crédito.")

usuarios = []  # Lista para armazenar os dados dos usuários
contas = {}    # Dicionário para armazenar as contas correntes

def criar_usuario(nome_completo, endereco, cpf, data_nascimento):
    """Cria um novo usuário com as informações fornecidas, garantindo que o CPF seja único."""
    # Verificar se o CPF já está registrado
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado.")
            return
    
    # Adicionar novo usuário
    novo_usuario = {
        "nome_completo": nome_completo,
        "endereco": endereco,
        "cpf": cpf,
        "data_nascimento": data_nascimento
    }
    usuarios.append(novo_usuario)
    
    # Inicializar conta corrente
    contas[cpf] = {
        "saldo": 0,
        "limite": 1000,
        "extrato": "",
        "numero_saque": 0,
        "limite_saque": 5
    }
    print(f"Usuário {nome_completo} criado com sucesso.")

def criar_conta_corrente(cpf):
    """Cria uma conta corrente para o usuário com o CPF fornecido."""
    if cpf not in [usuario['cpf'] for usuario in usuarios]:
        print("Usuário não encontrado. Crie um usuário primeiro.")
    elif cpf in contas:
        print("Conta corrente já existe para este usuário.")
    else:
        contas[cpf] = {
            "saldo": 0,
            "limite": 1000,
            "extrato": "",
            "numero_saque": 0,
            "limite_saque": 5
        }
        print(f"Conta corrente criada para o usuário com CPF {cpf}.")

def depositar(cpf, valor):
    """Deposita um valor na conta do usuário com o CPF fornecido."""
    conta = contas.get(cpf)
    
    if not conta:
        print("Conta não encontrada.")
        return
    
    if valor <= 0:
        print("Valor inválido para depósito.")
    else:
        conta["saldo"] += valor
        conta["extrato"] += f'Depósito: R$ {valor:.2f}\n'
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

def sacar(cpf, valor):
    """Saca um valor da conta do usuário com o CPF fornecido."""
    conta = contas.get(cpf)
    
    if not conta:
        print("Conta não encontrada.")
        return
    
    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > conta["limite"]
    excedeu_saques = conta["numero_saque"] >= conta["limite_saque"]
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor <= 0:
        print("Operação falhou! Valor informado é inválido.")
    else:
        conta["saldo"] -= valor
        conta["extrato"] += f'Saque: R$ {valor:.2f}\n'
        conta["numero_saque"] += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def extrato(cpf):
    """Exibe o extrato e o saldo da conta do usuário com o CPF fornecido."""
    conta = contas.get(cpf)
    
    if not conta:
        print("Conta não encontrada.")
        return
    
    print("\n==================== EXTRATO ====================")
    print("Não foram realizadas movimentações." if not conta["extrato"] else conta["extrato"])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("====================")

def credito(cpf):
    """Disponibiliza crédito baseado no saldo do usuário com o CPF fornecido."""
    conta = contas.get(cpf)
    
    if not conta:
        print("Conta não encontrada.")
        return
    
    if conta["saldo"] >= 1000:
        credito_disponivel = conta["saldo"] * 0.25
        print(f"Crédito disponível: R$ {credito_disponivel:.2f}")
    else:
        print("Saldo insuficiente para crédito.")

