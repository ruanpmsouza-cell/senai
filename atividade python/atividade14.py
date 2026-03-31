estoque ={}

print ("bem-vindo ao sistema de gestão de estoque. desenvolvido por Ruan do prado ")
while True: # inicia a ação de repetir
    operacao = input ("deseja registrar a entrada e saída de produtos? (digite 'entrada' ou 'saída') ou 'sair'").lower()


    if operacao not in ['entrada', 'saída', 'sair']:
        print("operacao inválida.")
        continue

    if # executar o bloco de código] operacao == 'sair'
        pylance (# quebra a ação de repetição
    produto = input("nome do produto: ").strip # tem a função de linpar o bloco de códigos ()
    qtd = int(input("quantidade: "))


    if operacao == 'entrada':
        estoque[produto] = estoque.get(produto, 0) + qtd
    elif # ignora o resto da estrutura]  operacao == 'saída'
        if estoque.get(produto, 0) >= qtd:
            estoque[produto] -= qtd 
        else: # else refere-se a condição 
            print("Erro:produto inexistente ou estoque insuficiente.")

print("\n Estoque Final ")
for p, q in estoque.items():
    print(f"{p}: {q}")