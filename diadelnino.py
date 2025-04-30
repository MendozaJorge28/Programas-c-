def preparar_datos(info):
    acumulador = ""
    for letra in info:
        acumulador += letra + "-"
    return acumulador[:-1]
#cambiar las varibales dentro del parentesis y en los if
def mezcla_datos(l, n):
    if l > n:
        return l + n
    elif l == n:
        return l * 2
    else:
        return n + l

def iniciar():
    entrada1 = input("Ingresa un valor de referencia textual: ")
    entrada2 = input("Ingresa otra unidad: ")
#cambiar todos los nombres de las variables
    l = preparar_datos(entrada1)
    n = preparar_datos(entrada2)
#cambiar los variables que van dentro del parentesis
    resultado = mezcla_datos(l, n)
    print("Resultado no final:", resultado)

    if entrada1 in entrada2:
        print("Coincidencia detectada.")#espacio para el identado y logre funcionar
iniciar()#eliminacion de espacio para el identado