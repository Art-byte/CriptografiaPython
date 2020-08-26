
import pyperclip

def main():
    mensaje = input('Introduce el mensaje: ')
    clave = int(input('y la clave numerica: '))
    mensaje = eliminar_espacios(mensaje)

    criptograma = salida(cifrar(mensaje,clave))

    print(criptograma.upper())
    pyperclip.copy(criptograma)


def eliminar_espacios(mensaje):
    mensaje_nuevo =''
    for simbolo in mensaje:
        if simbolo != '':
            mensaje_nuevo += simbolo
    return mensaje_nuevo


def salida(criptograma):
    bloque = 5
    texto = ''
    for i in range(len(criptograma)):
        if(i+1) % bloque != 0:
            texto += criptograma[i]
        else:
            texto += criptograma[i] + ''
    return texto


def cifrar(mensaje, clave):
    criptograma = [''] * clave
    
    for col in range(clave):
        pos = col
        while pos < len(mensaje):
            criptograma[col] += mensaje[pos]
            pos += clave
    return ''.join(criptograma)


if __name__ == "__main__":
    main()