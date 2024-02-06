aluno1 = input("Digite o nome do Primeiro aluno:  ")
media1 = float(input("Digite a media do Primeiro aluno: "))

while media1 < 0 or media1 > 10:
    media1 = float(input("Digite um valor entre 0 a 10: "))

aluno2 = input("Digite o nome do Segundo aluno:  ")
media2 = float(input("Digite a media do Segundo aluno: "))

while media2 < 0 or media2 > 10:
    media2 = float(input("Digite um valor entre 0 a 10: "))

aluno3 = input("Digite o nome do Terceiro aluno:  ")
media3 = float(input("Digite a media do Terceiro aluno: "))

while media3 < 0 or media3 > 10:
    media3 = float(input("Digite um valor entre 0 a 10: "))

if media1 > media2 and media1 > media3:
    maxmedia = media1
    aluno = aluno1
elif media2 > media1 and media2 > media3:
    maxmedia = media2
    aluno = aluno2
elif media3 > media1 and media3 > media2:
    maxmedia = media3
    aluno = aluno3

    
print(f"O aluno {aluno} teve a maior media {maxmedia}")
