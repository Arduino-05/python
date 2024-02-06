T = input("Digite o seu triglicérides:")
j = input("Vc esta em jejum:")
T = int(T)
j = str(j)


if j == "sim":
    if T <= 150:
        print("vc esta Normal")
    elif T > 150 and T <  199:
        print("vc esta  Moderado")
    elif T >= 200 and T < 499:
        print("vc esta Alto")
    elif T >= 500:
        print("vc esta morto")

else:
    if T <= 250:
        print("vc esta normal")
    elif T > 250 and T < 299:
        print("vc esta moderado")
    elif T >= 300 and T < 599:
        print("vc esta Alta")
    elif T > 600:
        print("vc esta morto")


        
