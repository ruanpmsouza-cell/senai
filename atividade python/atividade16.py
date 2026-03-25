numero = int(input("Digite um numero para abrir a tabuada : "))
print(f"\nTabuada do {numero}:\n")
for i in range(0, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")