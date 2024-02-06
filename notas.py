nome = input("Digite seu nome: ")
nome = str(nome)
nota_prova1 = float(input("Digite a nota da primeira prova: "))

while nota_prova1 < 0 or nota_prova1 > 10:
    nota_prova1 = float(input("Valor invalido Digite novamente: "))

    
nota_prova2 = float(input("Digite a nota da segunda prova: "))

while nota_prova2 < 0 or nota_prova2 > 10:
    nota_prova2 = float(input("Valor invalido. Digite novamente: "))
    
nota_Trabalho1 = float(input("Digite a nota da Terceira prova: "))

while nota_Trabalho1 < 0 or nota_Trabalho1 > 10:
    nota_Trabalho1 = float(input("Valor invalido Digite novamente: "))

media = nota_prova1 * 0.35 + nota_prova2 * 0.35 + nota_Trabalho1 * 0.3

if media >= 5:
    situacao = "Aprovado" 
elif media >= 3.5 and media < 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"
    

print(f"Ola {nome} sua media foi de {media} e sua situaçao e {situacao}")