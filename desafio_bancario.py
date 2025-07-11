menu = """

[d] Depositar
[s] Sacar 
[e] Extrato
[q] sair

=>  """

saldo = 0
limite = 500
extrato = ""
numero_saques=0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("Depósito")
        valor_digitado = input("Digite o valor que deseja depositar:\nR$ ")
        
        try: 
            deposito = float(valor_digitado)
   
            if deposito > 0:
                saldo += deposito # Adiciona o valor ao saldo
                extrato += f"Depósito: R$ {deposito:.2f}\n" # Registra no extrato
                print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
                print(f"\nTotal:R$ {saldo}")
            else: # O 'else' para a validação do depósito também precisa estar no mesmo nível do 'if'
                print("Operação falhou! O valor informado é inválido. Por favor, insira um valor positivo.")    
        except ValueError: 
            print("Erradão aí mano")

    elif opcao == "s":
        
        if numero_saques >= LIMITE_SAQUES:
            print("pode mais não man")
        
       
        
        else:
            print("Sacar")
            valor_digitado = input("Digite o valor que deseja Sacar:\nR$ ")
            
        
            try:
                saque = float(valor_digitado)
           
                if saque <= limite and saque <= saldo:
                    saldo -= saque
                    numero_saques += 1
                    extrato += f"Saque: R$ {saque:.2f}\n"
                    print(f"Saque de R$ {saque:.2f} Realizado com sucesso!")
                    print(f"\nTotal:R$ {saldo:.2f}")
                else: # O 'else' para a validação do depósito também precisa estar no mesmo nível do 'if'
                    print("Muito pobre mané kkkkkkk")    
            
            except ValueError: # O bloco 'except' deve estar no MESMO NÍVEL de indentação do 'try'
                print("Operação falhou! Valor inválido. Por favor, digite um número.")
        
        
    
    elif opcao == "e":
        print(extrato)
        print(f"\nTotal:R$ {saldo}")
        
    elif opcao == "q":
        print('Sair')    