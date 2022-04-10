def calculo_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc


def pedir_datos():
    peso = float(input('Dinos tu peso por favor: '))
    altura_en_centimetros = float(input('Dinos tu altura por favor: '))
    altura_en_metros = altura_en_centimetros / 100
    imc = calculo_imc(peso, altura_en_metros)

    if imc < 19:
        print('Estado de Delgades')
    elif imc > 19 and imc < 26:
        print('Estado Normal')
    elif imc > 25 and imc < 31:
        print('Estado de Sobrepeso')
    else:
        print('Estado de Obesidad')


pedir_datos()
