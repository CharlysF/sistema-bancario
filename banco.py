menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
[5] Crédito
=> """

saldo = 0
limite = 1000
extrato = ""
numero_saque = 0
limite_saque = 5
limite_credito = 0  # Variável para armazenar o limite de crédito

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print("Operação falhou: o valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= limite_saque

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saque += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n==================== EXTRATO ====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================================")

    elif opcao == "4":
        break

    elif opcao == "5":
        if saldo >= 1000:
            limite_credito = saldo * 0.25
            print(f"Você tem direito a um limite de crédito de R$ {limite_credito:.2f}.")
        else:
            print("Operação falhou! Saldo insuficiente para disponibilizar crédito.")

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
