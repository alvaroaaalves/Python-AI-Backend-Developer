Clientes = {'Clientes'}

def criar_usuario(Clintes):
    nome = input("Digite o nome do Cliente:> ")
    cpf = input("Digite o CPF do Cliente:> ")
    senha = input("Digite a senha de sua conta:> ")

    novo_cliente = [nome,cpf,senha]
    print (novo_cliente)
    Clientes.add((novo_cliente))
    return (Clientes)


print(Clientes)
criar_usuario(Clientes)
print(Clientes)
