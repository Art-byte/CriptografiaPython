import pyperclip

print('Este programa cifra o decifra un mensaje mediante la cifra de cesar')

ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
salida =''

modo = input('Desea cifrar o decifrar? (c/D)')
texto = input('Introduce el texto: ')

clave = int(input('Y la clave (1-25): '))

#ejecucion letra por letra
for simbolo in texto.upper():
    if simbolo in ALFABETO:
        pos = ALFABETO.find(simbolo)

        if modo == "c":
            pos = (pos + clave) % 26

        elif modo == "D":
            pos =(pos - clave) % 26
        salida += ALFABETO[pos]

    else:
        salida += simbolo

print(salida)
pyperclip.copy(salida)
    

