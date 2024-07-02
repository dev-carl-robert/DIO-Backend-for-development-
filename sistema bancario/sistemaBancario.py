<<<<<<< HEAD
from datetime import datetime, time, date, timedelta

saldo = 0
paraSistema = True
valorSaque = 0
valorDeposito = 0
limite = 500
limiteDeSaque = 10
data_extrato = None

while paraSistema == True:
    print('''
Bem vindo ao Banco Payseg
escolha:
[1] Sacar
[2] Depositar
[3] Ver extrato
[4] Sair
            ''')
    operacao = int(input("Como podemos lhe ajudar? "))


    if operacao == 2:
        print(" ")
        valorDeposito = float(input("Quanto voce deseja depositar: "))
        saldo = saldo + valorDeposito
        print(" ")
        print(f"R$ {valorDeposito:.2f} depositado com sucesso \n Seu saldo atual é : R$ {saldo:.2f}")
    elif operacao == 1:
        print(" ")
        valorSaque = float(input("Quanto você deseja sacar?  "))
        if valorSaque <= saldo:
            if saldo - valorSaque >= 0:    
                saldo -= valorSaque
                print(" ")
                print(f"R$ {valorSaque:.2f} sacado com sucesso, você tem em conta R$ {saldo:.2f} \n saques restantes {limiteDeSaque - 1}")
                limiteDeSaque -= 1
            else: 
                print(" ")
                print("saldo insuficiente")
        if valorSaque > limite:
            print(" ")
            print("valor de saque diario excedido")
        if limiteDeSaque < 0:
            print(" ")
            print("limite maximo de saques diario atigindo")
    elif operacao == 3:
        print(" ")
        print(f'''
    Seu saldo atual é R$ {saldo:.2f}.
    Voce depositou R$ {valorDeposito:.2f}.
    Voce sacou R$ {valorSaque:.2f}.
              ''')
    else:
        paraSistema = False
        print(" ")
        print("obrigado pela preferencia")
=======
saldo = 0
paraSistema = True
valorSaque = 0
valorDeposito = 0
limite = 500
limiteDeSaque = 3

while paraSistema == True:
    print('''
Bem vindo ao Banco Payseg
escolha:
[1] Sacar
[2] Depositar
[3] Ver extrato
[4] Sair
            ''')
    operacao = int(input("Como podemos lhe ajudar? "))


    if operacao == 2:
        print(" ")
        valorDeposito = float(input("Quanto voce deseja depositar: "))
        saldo = saldo + valorDeposito
        print(" ")
        print(f"R$ {valorDeposito:.2f} depositado com sucesso \n Seu saldo atual é : R$ {saldo:.2f}")
    elif operacao == 1:
        print(" ")
        valorSaque = float(input("Quanto você deseja sacar?  "))
        if valorSaque <= saldo:
            if saldo - valorSaque >= 0:    
                saldo -= valorSaque
                print(" ")
                print(f"R$ {valorSaque:.2f} sacado com sucesso, você tem em conta R$ {saldo:.2f} \n saques restantes {limiteDeSaque - 1}")
                limiteDeSaque -= 1
            else: 
                print(" ")
                print("saldo insuficiente")
        if valorSaque > limite:
            print(" ")
            print("valor de saque diario excedido")
        if limiteDeSaque < 0:
            print(" ")
            print("limite maximo de saques diario atigindo")
    elif operacao == 3:
        print(" ")
        print(f'''
    Seu saldo atual é R$ {saldo:.2f}.
    Voce depositou R$ {valorDeposito:.2f}.
    Voce sacou R$ {valorSaque:.2f}.
              ''')
    else:
        paraSistema = False
        print(" ")
        print("obrigado pela preferencia")
>>>>>>> 0020aee41afcea1bbeb5f4d05f5fcf334c8c9c6a
