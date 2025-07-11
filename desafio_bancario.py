# -*- coding: utf-8 -*-
"""
Sistema Bancário Simples

Este programa simula as operações básicas de um caixa eletrônico:
depósito, saque e extrato.

Restrições:
- Saques:
  - Limite máximo de R$ 500,00 por saque.
  - Limite de 3 saques por dia.
  - Não é possível sacar se o saldo for insuficiente.
- Depósitos:
  - Apenas valores positivos são aceitos.
- Extrato:
  - Exibe o histórico de transações e o saldo atual.
"""

menu = """

[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair

=> """

saldo = 0.0  # Usar float para saldo, garantindo precisão monetária
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3  # Constante para o limite de saques diários

while True:
    opcao = input(menu).lower()  # Converte a entrada para minúscula para flexibilidade

    if opcao == "d":
        print("\n--- OPERAÇÃO: DEPÓSITO ---")
        valor_str = input("Informe o valor a ser depositado:\nR$ ")

        try:
            deposito = float(valor_str)

            if deposito > 0:
                saldo += deposito
                # Registra a transação no extrato
                extrato += f"Depósito: \tR$ {deposito:.2f}\n" 
                print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
                print(f"Saldo atual: R$ {saldo:.2f}")
            else:
                print("Operação falhou! O valor informado é inválido. Por favor, insira um valor positivo.")
        except ValueError:
            print("Operação falhou! Valor inválido. Por favor, digite um número para o depósito.")

    elif opcao == "s":
        print("\n--- OPERAÇÃO: SAQUE ---")
        
        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Limite diário de saques excedido.")
            continue # Volta para o início do loop sem pedir o valor do saque

        valor_str = input("Informe o valor a ser sacado:\nR$ ")
        
        try:
            saque = float(valor_str)

            if saque <= 0:
                print("Operação falhou! O valor informado é inválido. Por favor, insira um valor positivo.")
            elif saque > saldo:
                print("Operação falhou! Você não possui saldo suficiente.")
                print(f"Seu saldo atual é: R$ {saldo:.2f}")
            elif saque > limite:
                print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f} por operação.")
            else:
                saldo -= saque
                numero_saques += 1
                # Registra a transação no extrato
                extrato += f"Saque: \t\tR$ {saque:.2f}\n" 
                print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
                print(f"Saldo atual: R$ {saldo:.2f}")
        except ValueError:
            print("Operação falhou! Valor inválido. Por favor, digite um número para o saque.")

    elif opcao == "e":
        print("\n--- EXTRATO ---")
        if not extrato:  # Verifica se a string extrato está vazia
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("------------------")

    elif opcao == "q":
        print("\nObrigado por usar nosso sistema bancário. Volte sempre!")
        break  # Sai do loop while

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
