#python3 dicionario.py

clientes = [
    {"nome":"Ana","cel":"11 54554-6767","empresa":"Agel"},
    {"nome":"Pedro","cel":"11 67435-6969","empresa":"Itau"}
]

empresa_pesquisada = (input ("Qual empresa voce procura? "))

for cliente in clientes:
    if cliente["empresa"] == empresa_pesquisada:
        print (cliente)

# Cadastrar novo cliente

print ("---> Cadastrar um novo cliente <---")
nome = input ("Digite o nome do cliente: ")
celular = input ("Digite o numero de celular do cliente: ")
empresa = input ("Digite de qual empresa o cliente faz parte: ")
    

novo_cliente = {
    "nome": nome,
    "cel": celular,
    "empresa": empresa
}
clientes.append(novo_cliente)
print (clientes)

# Remover um cliente
print ("---> Cadastrar um cliente pelo Nome <---")
nome_cliente = input ("Digite o nome do cliente para remover: ")

for cliente in clientes:
    if cliente["nome"] == nome_cliente:
        clientes.remove (cliente)
        break

print (clientes)
