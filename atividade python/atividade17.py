tipo = 0
tipo_de_usuario = 0
membro = tipo_de_usuario
liberado = membro
# começo apresentando o sistema
print(" Bem-vindo ao Sistema de Acesso ")
# declaração de informação de usuário
tipo_de_usuario = input(" você é 'membro' ou 'visitante':")
# declaração dos dias de funcionamento
dia = input(" Digite o dia da semana, de 'segunda' a 'domingo' ")
# declaração dos horarios de atendimento 
hora = int(input(" Digite o horário  "))
# verificação se acesso inválido
acesso, erro = False, " Acesso inválido !!"
# declaração dos dias de funcionamento de visitantes ou membros
if dia in ['sábado', 'sabado', 'domingo']: 
    # declaração de membro
    if tipo == 'membro': acesso = True
    # declaração de erro caso usuário for visitante e for diferente do fim de semana
    else: erro = "Visitantes não tem acesso a os fins de semana "
# declaração de acesso liberado a membros liberados nos dias de semana
elif dia in ['segunda', 'terça', 'terca', 'quarta', 'quinta', 'sexta']:
    # verificação de horário de funcionamento 
    if not (9 <= 18):
        # horario deve estar entre as 09 as 18 horas
        erro = "Sistema fechado (09h às 18h)."
        # caso esteja tudo certo o membro entrara sem problemas
    elif tipo == 'membro':
        # caso tudo esteja certo o sistema respondera acesso liberado
        acesso = True
        print(f"(seu acesso  foi {liberado}")

                # verificação das normas do visitante
    elif tipo == 'visitante':
    # verificação dos horarios se condizem com o usuario visitante 
        tempo = int(input("Quanto tempo deseja ficar? (horas): "))
    # verificação do tempo se condiz como usuario visitante 
        if tempo <= 4 and (hora + tempo <= 18):
        # caso horario e tempo corretos ele ira liberar o acesso de visitantes 
            acesso = True
        else:
        # verificação se horario esta diferente do modo de visitantes
            erro = "Visitantes: máximo 4h e saída até as 18h."
else:
# verificação de dias de acesso liberado a visitantes se estiver incorreto 
    erro = "Dia da semana inválido."
    # aqui ele dira se o usuario pode ou nao entrar no sistema
    if acesso:
        print(" Acesso liberado! ")
    else:
        print(f" Acesso negado: {erro} ")