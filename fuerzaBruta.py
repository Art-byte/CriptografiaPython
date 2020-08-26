
ALFABETO= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

criptograma = input('criptograma: ')
for clave in range(1,len(ALFABETO)):

    salida = ''
    for simbolo in criptograma:
        if simbolo in ALFABETO:
            pos = ALFABETO.find(simbolo)   
            pos = (pos - clave)%len(ALFABETO)

            salida += ALFABETO[pos]
        else:
            salida += simbolo
    print('Clave %d: %s' % (clave, salida))



