import math, pyperclip

def main():
    criptograma = input("ingresa el criptograma: ")
    clave = int(input("Ingresa la clave numerica: "))
    criptograma = formatear_mensaje(criptograma)

    texto_plano = decifrar(criptograma,clave)

    print(texto_plano.lower())
    pyperclip.copy(criptograma)



def formatear_mensaje(criptograma):
    mensaje_nuevo =''
    for simbolo in criptograma:
        if simbolo != ' ':
            mensaje_nuevo += simbolo
    return mensaje_nuevo

def decifrar(criptograma, clave):
    num_col = math.ceil(len(criptograma)/clave)
    num_filas = clave

    celdas_vacias = (num_col * num_filas) - len(criptograma)

    texto_plano = [""] * num_col
    col = 0
    fila = 0 

    for simbolo in criptograma:
        texto_plano[col] += simbolo
        col += 1 #siguiente columna 

        #Si no hay mas columnas o estamos en una celda sobrante
        #nos regresamos a la primer columna de la siguiente fila 

        if(col == num_col)or(col == num_col -1 and fila >= num_filas - celdas_vacias):
            col = 0
            fila += 1
    return ''.join(texto_plano)

if __name__ == "__main__":
    main()



