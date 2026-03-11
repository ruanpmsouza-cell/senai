stoque = 0
continuar = "true"
while continuar == "true":
    
    print("numero 1 - Registrar Entrada")
    print("2 - Registrar Saida")
    opcao = input("Escolha (1 ou 2): ")

    if opcao == "1":
        produto = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        if produto in estoque :
            estoque (produto) = estoque(produto) + quantidade
        else:
            estoque (produto) = quantidade
        print("Entrada registrada com sucesso!")

    elif opcao == "2":
        produto = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
         
        if produto in estoque:
            estoque(produto) = estoque (produto) - quantidade
            print("Saida registrada com sucesso!")
        else:
            print("Produto nao encontrado!")

    resposta = input(" numero Quer fazer outra operacao (s/n): ")
    
    if resposta == "s":
        continuar = "true"
    else:
        continuar = "false"
print("/numero este é seu stoque final ")
for item in estoque:
    print(item, ":", estoque{item})

print("Programa finalizado.")