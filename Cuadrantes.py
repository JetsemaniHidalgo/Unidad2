# Definimos una lista que contiene las etiquetas de los cuadrantes y el mensaje para el origen del sistema de coordenadas.
cuadrantes = ['Origen', 'Eje Y', 'Eje X', 'Cuadrante I', 'Cuadrante II', 'Cuadrante III', 'Cuadrante IV']

# Creamos un bucle infinito usando "while True" para que el programa se repita continuamente hasta que se rompa.
while True:
    # Solicitamos al usuario que ingrese los valores de 'x' e 'y' y los convertimos a enteros usando int().
    x = int(input('Ingresa el valor de x: '))
    y = int(input('Ingresa el valor de y: '))

    # Evaluamos las coordenadas para determinar en qué cuadrante se encuentra el punto.
    if x == 0 and y == 0:
        print(cuadrantes[0])  # Si ambos valores son cero, el punto está en el origen.
    elif x == 0:
        print(cuadrantes[1])  # Si 'x' es cero, el punto está en el eje Y.
    elif y == 0:
        print(cuadrantes[2])  # Si 'y' es cero, el punto está en el eje X.
    elif x > 0 and y > 0:
        print(cuadrantes[3])  # Si 'x' e 'y' son mayores que cero, el punto está en el Cuadrante I.
    elif x < 0 and y > 0:
        print(cuadrantes[4])  # Si 'x' es menor que cero y 'y' es mayor que cero, el punto está en el Cuadrante II.
    elif x < 0 and y < 0:
        print(cuadrantes[5])  # Si ambos valores son menores que cero, el punto está en el Cuadrante III.
    elif x > 0 and y < 0:
        print(cuadrantes[6])  # Si 'x' es mayor que cero y 'y' es menor que cero, el punto está en el Cuadrante IV.
    else:
        print('El punto está en el origen del sistema de coordenadas.')  # Si ninguna condición se cumple, el punto está en el origen.

    # Preguntamos al usuario si desea hacer otra consulta o no, almacenando su respuesta en la variable 'continuar'.
    continuar = input("¿Deseas hacer otra consulta? (s/n): ")

    # Comparamos la respuesta del usuario con 's' (sin importar si está en mayúscula o minúscula).
    # Si la respuesta no es 's', rompemos el bucle usando "break" y finalizamos el programa.
    if continuar.lower() != 's':
        break
