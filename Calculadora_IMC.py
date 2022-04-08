def calculo_imc(peso, altura):
    imc = peso / (altura * altura)
    print(imc)

    if imc < 19:
        print('Estado de Delgades')
    elif imc > 19 and imc < 26:
        print('Estado Normal')
    elif imc > 25 and imc < 31:
        print('Estado de Sobrepeso')
    else:
        print('Estado de Obesidad')


peso = float(input('Dinos tu peso por favor: '))
altura = float(input('Dinos tu altura por favor: '))
altura = altura / 100

calculo_imc(peso, altura)
