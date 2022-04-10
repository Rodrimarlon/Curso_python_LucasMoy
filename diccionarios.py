numeros = {
    '0': 'cero',
    '1': 'uno',
    '2': 'dos',
    '3': 'tres',
    '4': 'cuatro',
    '5': 'cinco',
    '6': 'seis',
    '7': 'siete',
    '8': 'ocho',
    '9': 'nueve'
}

seguir_buscando = True
texto_final = ''


while seguir_buscando == True:
    texto = (input('Introduce un número: '))
    if texto == 'salir':
        seguir_buscando = False
        print('Gracias por Participar')

    else:
        for letra in texto:
            texto_final += numeros[letra] + ' '
        print(texto_final)
    texto_final = ''
