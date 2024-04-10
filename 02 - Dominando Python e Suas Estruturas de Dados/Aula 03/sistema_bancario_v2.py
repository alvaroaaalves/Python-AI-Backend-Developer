import datetime
import time
print (datetime.datetime.now())

NOME             = input ("Digite seu Nome: ").title()
limite           = 1500
saldo            = 0
QUANTIDADE_SAQUE = 5
quantidade_saque = 0
extrato          = []
######################################################################
def menu_principal (NOME):
    return(input (f"""
            O que deseja fazer Sr(a) {NOME}
            [d] - DEPOSITAR
            [s] - SACAR
            [e] - VERIFICAR SEU EXTRATO
            [q] - ENCERRAR ATENDIMENTO

            Digite a opção :>  """).upper())
######################################################################
def sacar(valor_saque,limite,saldo,extrato):
    if (valor_saque > saldo):
        print (f"SALDO INSUFICIENTE, seu saldo é {saldo:.2f}")
    elif():
        print (f"LIMITE INSUFICIENTE, seu limite atual é {limite:.2f}")
    elif(valor_saque <= saldo and valor_saque > 0):
        limite -= valor_saque
        saldo  -= valor_saque
        extrato.append(atualizar_extrato("Saque", extrato, valor_saque))
    else:
        print ("Valor invalido")
    return (saldo,limite,extrato)
######################################################################
def depositar(saldo, valor_depositado,extrato):
    if (valor_depositado <= 0):
        print("Não é possivel depositar esse valor")
    else:
        saldo = saldo + valor_depositado
        extrato.append(atualizar_extrato("Deposito", extrato, valor_depositado))
    return (saldo,extrato)
######################################################################
def exibir_extrato (extrato,saldo):
    print (f"\n##### Extrato de {NOME} #####")
    for item in (extrato):
        print (f"{item[0]} de R$ {item[1]:.2f} em {item[2]}")
    print (f"\nSaldo atual R$ {saldo:.2f}\n")
######################################################################
def atualizar_extrato(Tipo, extrato, valor):
    inserir = [Tipo, valor, datetime.datetime.now()]
    return (inserir)
######################################################################



while(True):
    opcao = menu_principal(NOME)
    if (opcao == 'Q'):
        print (f"Encerrado antendimento de {NOME}")
        break
        
    elif (opcao == 'E'):
        exibir_extrato(extrato,saldo)        

    elif (opcao == 'D'):
        valor_depositado = float(input("Digite o valor a ser depositado: "))
        saldo, extrato = depositar(saldo,valor_depositado,extrato)

    elif (opcao == 'S'):
        if (QUANTIDADE_SAQUE >= 1):
            valor_saque = float(input("Digite o valor a ser sacado: "))
            saldo,limite,extrato = sacar(valor_saque,limite,saldo,extrato)
            QUANTIDADE_SAQUE -= 1
        else:
            print ("Você já sacou seu limite de vezes hoje")
            
        
