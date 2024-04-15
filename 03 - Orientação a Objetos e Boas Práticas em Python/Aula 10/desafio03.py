class Plano():
    def __init__(self, saldo_inicial):
            self.saldo = saldo_inicial

class UsuarioTelefone(Plano):
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        super().__init__(plano)

    def verificar_saldo(self):
        if (self.saldo_inicial < 10):
            return (self.saldo_inicial,"Seu saldo está baixo. Recarregue e use os serviços do seu plano.")
        elif (self.saldo_inicial >= 50):
            return (self.saldo_inicial,"Parabéns! Continue aproveitando seu plano sem preocupações.")
        else:
            return (self.saldo_inicial,"Seu saldo está razoável. Aproveite o uso moderado do seu plano.")
'''
class PlanoTelefone():
    def __init__(self, plano, saldo_inicial):
        self.plano = plano
        self.saldo_inicial = saldo_inicial  
'''
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self,nome, numero, saldo_inicial):
        self.nome = nome
        self.numero = numero
        self.saldo_inicial = saldo_inicial
        super().__init__(nome, numero, Plano(saldo_inicial))

    def fazer_chamada(self, destinatario, duracao):
        custo = duracao*0.10
        if (custo <= self.saldo_inicial):
            self.saldo_inicial = saldo_inicial-custo
            #print(self.saldo_inicial)
            return (f'Chamada para {destinatario} realizada com sucesso. Saldo: ${self.saldo_inicial:.2f}')
        else:
            return ("Saldo insuficiente para fazer a chamada.")

        


'''
nome = input()
numero = input()
saldo_inicial = float(input())
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
'''
nome = "Alvaro"
numero = "(85) 98505-4244"
saldo_inicial = 10.00
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = "(33) 93333-3333"
duracao = 60
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
