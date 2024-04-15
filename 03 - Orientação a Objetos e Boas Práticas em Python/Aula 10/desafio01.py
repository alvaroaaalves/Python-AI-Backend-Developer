
class UsuarioTelefone():
    def __init__ (self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano
        
    def __str__(self):
        return (f"Usuário {self.nome} criado com sucesso.")


nome = input("Nome: ")  
numero = input("Número: ")  
plano = input("Plano: ")

        
user = UsuarioTelefone(nome,numero,plano)
print (user)

