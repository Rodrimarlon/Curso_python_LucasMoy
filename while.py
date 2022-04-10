
def chat():
    seguir_chateando = True

    while seguir_chateando:
        texto = input('>')

        if texto == 'salir':
            seguir_chateando = False

        texto = texto.replace(':)', '🙂')
        texto = texto.replace(':(', '🙁')
        print(texto)


chat()
