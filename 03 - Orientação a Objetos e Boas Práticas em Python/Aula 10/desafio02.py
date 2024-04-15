class UsuarioTelefone():
    def __init__(self, nome, plano):
        self.nome = nome
        self.nome_plano = plano.plano
        self.saldo_inicial = plano.saldo_inicial

    def verificar_saldo(self):
        if (self.saldo_inicial < 10):
            return (self.saldo_inicial,"Seu saldo está baixo. Recarregue e use os serviços do seu plano.")
        elif (self.saldo_inicial >= 50):
            return (self.saldo_inicial,"Parabéns! Continue aproveitando seu plano sem preocupações.")
        else:
            return (self.saldo_inicial,"Seu saldo está razoável. Aproveite o uso moderado do seu plano.")
        


class PlanoTelefone():
    def __init__(self, plano, saldo_inicial):
        self.plano = plano
        self.saldo_inicial = saldo_inicial  
        



nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)
