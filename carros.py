carros = ['Vectra', 'Astra', 'Palio', 'Saveiro', 'Masserati']


def mos():
    for idx in range(len(carros)):
        print(f'{idx}, {carros[idx]}')
    
rmv = int(input(f'Quer comprar qual? '))

del carros[rmv]

for idx in range(len(carros)):
    print(f'{idx} {carros[idx]}')

