senha_correta = "123456"
tentativas_restantes = 3
nome = input("Digite seu nome: ")
while tentativas_restantes > 0:
    senha_digitada = input("Digite sua senha: ")
    if senha_digitada == senha_correta:
        print(f"Olá, {nome}, seja bem-vindo ao nosso banco.")
        break
    else:
        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print(f"Senha incorreta. Você ainda tem {tentativas_restantes} {'tentativa' if tentativas_restantes == 1 else 'tentativas'}.")
        else:
            print(f"Senha incorreta. {nome}, sua conta foi bloqueada. Por favor, dirija-se aos nossos caixas.")