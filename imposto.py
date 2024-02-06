salario = input("Digite seu Salario: ")
salario = int(salario)

if salario <= 2112:
    print("Vc eh pobre cara!")
elif salario > 2112 and salario <= 2826:
    imposto = salario * (7.5/100)
    valortotal = salario - imposto
elif salario > 2826 and salario <= 3751:
    imposto = salario * 0.15
    valortotal = salario - imposto
elif salario > 3751 and salario <= 4664:
    imposto = salario * 0.22
    valortotal = salario - imposto
elif salario > 4664:
    imposto = salario * 0.27
    valortotal = salario - imposto
    
print(f"Seu imposto sera de {imposto}, E seu salario liquido e de {valortotal} ")
