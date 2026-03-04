nome = input ("  insira o seu nome :  ")
idade = int (input("digite sua idade :  "))

#repete quando a idade for valida
while idade > 120 or idade < 0:
    print = int(input("idade (anos completos - ate 120): "))
dias_vida = idade * 365 
print(f"{nome}, voce viveu {dias_vida} ")


