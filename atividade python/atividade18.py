#  fala de seja bem-vindo e apresenta o sistema 
print(" Bem-vindo ao Sistema de Acesso ")

# Declaração de informação de usuário
tipo_de_usuario = input(" você é 'membro' ou 'visitante': ").strip()

# Declaração dos dias de funcionamento
dia = input(" Digite o dia da semana, de 'segunda' a 'domingo': ")

# Declaração dos horarios de atendimento 
hora = int(input(" Digite o horário de entrada : "))

# Verificação se acesso inválido 
acesso, erro = False, " Acesso inválido !!"

# Verificação de Final de Semana para visitantes
if dia in ['sábado', 'sabado', 'domingo']: 
    # verificação de dados de visitantes a os fins de semana
    if tipo_de_usuario == 'membro': 
        acesso = True
    else: 
        # fala de visitantes com o acesso negado ha os fins de semana
        erro = "Visitantes não têm acesso aos fins de semana."

# Verificação de Dias de Semana para membros
elif dia in ['segunda', 'terça', 'terca', 'quarta', 'quinta', 'sexta']:
    # verificação de horarios  de funcionamendo de membros 
    if not (9 <= hora <= 18):
        erro = "Sistema fechado (Horário de funcionamento: 09h às 18h)."
    # verificação de usuario se visitante ou membro
    elif tipo_de_usuario == 'membro':
        acesso = True
        # confirmação de acesso ha membros 
        print("Seu acesso foi liberado!") 
        
    elif tipo_de_usuario == 'visitante':
        # verificação de tempo de visitantes
        tempo = int(input("Quanto tempo deseja ficar? (horas): "))
        # Visitante só entrar apos as 4 e sair apos as 18 horas 
        if tempo <= 4 and (hora + tempo <= 18):
            #  ele ira dizer acesso liberado ou nao
            acesso = True
        else:
            # verificação de horarios de visitantes
            erro = "Visitantes: máximo 4h e saída até as 18h."
else:
    # resultado de dias de funcionamento invalidos sistema ira digitar invalido 
    erro = "Dia da semana inválido."

# Exibição do resultado final se acesso liberado ou nao 
if acesso:
    print(" seja bem-vindo a o sistema  ")
else:
    print(f" Acesso negado: {erro} ")