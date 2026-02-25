contador = 0
soma = 0
while contador < 4:
    contador += 1
    nota = float (input (f"insira o {contador} nota "))
    soma+=nota

media = nota/contador
print ("a media das notas : ",media )
if media >= 7:
    print("aluno esta aprovado !!")
else:
    print("aluno esta reprovado")
