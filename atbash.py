import pyperclip

#Alfabetos empleados
CLARO = 'abcdefghijklmnopqrstuvwxyz'
CIFRADO ='ZYXWVUTSRQPONMLKJIHGFEDCBA'

#Almacena la forma cifrada/decifrada del mensaje
salida = '' 

texto = input('Introduce un mensaje: ')

#Ejecutar el cifrado 
for simbolo in texto.lower():
    if simbolo in CLARO:
        #identificamos la posicion de cada simbolo

        indice = CLARO.index(simbolo)
        salida += CIFRADO[indice]

print(salida)
pyperclip.copy(salida)
    