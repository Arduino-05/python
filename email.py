email = input("Digite seu email: ")
nome = input("Digite seu Nome: ")

titulo = input("Digite o titulo: ")
assunto = input("Escreva um assunto: ")

pergunta = input(f"Vc gostaria de falar do assunto {assunto}: ")

if pergunta == "sim":
    print("Estamos em desenvolvimento") 
else:
    print(f"Atenciosamente {nome} por {email}")