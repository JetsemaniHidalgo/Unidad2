# Unidad2
En esta unidad, se desarrollaron dos productos de aprendizaje.

El primer producto consiste en verificar dos condiciones a partir de una palabra ingresada por el usuario. El rango de caracteres permitidos para la palabra se define en una tupla llamada rango_caracteres_permitidos = (4, 8), lo que nos permite realizar la validación de las condiciones. Esto se logra gracias a la instrucción "len", que nos permite contar la cantidad de caracteres.

La primera verificación consiste en comprobar si la palabra ingresada tiene entre cuatro y ocho caracteres. Si se cumple esta condición, se le indica al usuario que la palabra es correcta. Esta comprobación se realiza mediante la siguiente instrucción:
if rango_caracteres_permitidos[0] <= Longitud <= rango_caracteres_permitidos[1]:
La segunda condición verifica si la palabra tiene menos de cuatro caracteres. Si es así, se le indica al usuario cuántos caracteres tiene su palabra y también cuántos caracteres le faltan para llegar al mínimo requerido de cuatro caracteres. Esto se verifica con la siguiente instrucción:
elif Longitud < rango_caracteres_permitidos[0]:
La tercera condición verifica si la palabra tiene más de ocho caracteres. Si es así, se le indica al usuario cuántos caracteres tiene su palabra y también cuántos caracteres le sobran para alcanzar el máximo de ocho caracteres permitidos. Esto se verifica con la siguiente instrucción:
else: # Ya que solo nos queda comparar si es mayor a 8

El segundo producto de aprendizaje consiste en una herramienta para ayudar a determinar la ubicación de un punto en un sistema de coordenadas cartesianas y permite al usuario realizar múltiples consultas si lo desea.
Se define una  lista llamada "cuadrantes" que contiene las etiquetas para cada cuadrante y el origen del sistema de coordenadas y se inicia un while True, lo que significa que el código dentro se ejecutará repetidamente hasta que se alcance una condición de ruptura.

Dentro del While, el programa solicita al usuario que ingrese los valores de 'x' e 'y' del punto que se quiere ubicar y posteriormente se evalúan los valores de 'x' e 'y' para determinar en qué cuadrante se encuentra el punto, o si está en el origen o en algún eje del sistema de coordenadas, dependiendo de los valores ingresados, se imprime un mensaje que indica en qué cuadrante se encuentra el punto o si está en el origen o en algún eje. Después de imprimir la ubicación del punto, el programa le pregunta al usuario si desea realizar otra consulta. Si el usuario ingresa 's' (sin importar si es en mayúscula o minúscula), el programa vuelve al principio del bucle para que el usuario pueda ingresar nuevos valores. Si el usuario no ingresa 's', el programa utiliza el comando break para salir del bucle infinito, lo que significa que el programa se detendrá y finalizará.



