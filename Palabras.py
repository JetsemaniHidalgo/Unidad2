while True:
    # Solicitamos al usuario que ingrese una palabra
    Palabra = input("Introduce una palabra: ")
    
    # Calculamos la longitud de la palabra ingresada por el usuario
    Longitud = len(Palabra)
    
    # Mostramos la cantidad de caracteres en la palabra ingresada
    print("La cantidad de caracteres en la palabra son:", Longitud)

    # Definimos una tupla para almacenar el rango mínimo y máximo de caracteres permitidos
    rango_caracteres_permitidos = (4, 8)
    
    # Verificamos si la longitud de la palabra está dentro del rango permitido
    if rango_caracteres_permitidos[0] <= Longitud <= rango_caracteres_permitidos[1]:
        # Si está dentro del rango, mostramos un mensaje de palabra correcta
        print("La palabra es correcta, está dentro del rango.")
    elif Longitud < rango_caracteres_permitidos[0]:
        # Si es menor que el mínimo, calculamos cuántas letras faltan para alcanzarlo
        faltan_letras = rango_caracteres_permitidos[0] - Longitud
        print("Faltan letras, usted ingresó", Longitud, "caracteres.")
        print("Faltan", faltan_letras, "letras para alcanzar el mínimo de 4 caracteres.")
        print("Palabra ingresada:", Palabra)
    else:
        # Si es mayor que el máximo, calculamos cuántas letras sobran que exceden el máximo
        sobran_letras = Longitud - rango_caracteres_permitidos[1]
        print("Sobran letras, usted ingresó:", Longitud, "caracteres.")
        print("Sobran", sobran_letras, "letras que exceden el máximo de 8 caracteres.")
        # Mostramos solo los primeros 8 caracteres de la palabra y agregamos puntos suspensivos
        print("Palabra ingresada:", Palabra[:rango_caracteres_permitidos[1]], "...")
        # Mostramos las letras que sobran después de los primeros 8 caracteres
        print("Letras que sobran:", Palabra[rango_caracteres_permitidos[1]:])

    # Preguntamos al usuario si quiere comprobar otra palabra
    continuar = input("¿Desea comprobar otra palabra? (si/n): ")
    
    # Si la respuesta es "no" o "n", salimos del bucle y terminamos el programa
    if continuar.lower() == "no" or continuar.lower() == "n":
        break
    
    # Agregamos una línea en blanco para separar cada iteración del bucle
    print()
