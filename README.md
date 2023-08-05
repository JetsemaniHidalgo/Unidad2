# Unidad2
En esta unidad, se desarrollaron dos productos de aprendizaje.

El primer producto consiste en verificar dos condiciones a partir de una palabra ingresada por el usuario. El rango de caracteres permitidos para la palabra se define en una tupla llamada rango_caracteres_permitidos = (4, 8), lo que nos permite realizar la validación de las condiciones. Esto se logra gracias a la instrucción "len", que nos permite contar la cantidad de caracteres.

La primera verificación consiste en comprobar si la palabra ingresada tiene entre cuatro y ocho caracteres. Si se cumple esta condición, se le indica al usuario que la palabra es correcta. Esta comprobación se realiza mediante la siguiente instrucción:
if rango_caracteres_permitidos[0] <= Longitud <= rango_caracteres_permitidos[1]:
La segunda condición verifica si la palabra tiene menos de cuatro caracteres. Si es así, se le indica al usuario cuántos caracteres tiene su palabra y también cuántos caracteres le faltan para llegar al mínimo requerido de cuatro caracteres. Esto se verifica con la siguiente instrucción:
elif Longitud < rango_caracteres_permitidos[0]:
La tercera condición verifica si la palabra tiene más de ocho caracteres. Si es así, se le indica al usuario cuántos caracteres tiene su palabra y también cuántos caracteres le sobran para alcanzar el máximo de ocho caracteres permitidos. Esto se verifica con la siguiente instrucción:
else: # Ya que solo nos queda comparar si es mayor a 8



