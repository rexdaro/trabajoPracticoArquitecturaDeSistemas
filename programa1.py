# Ejercicio 1: Simulación de Interacción E/S (Teclado y Pantalla)

# Ejercicio 1: Simulación de Interacción E/S (Teclado y Pantalla)
# Descripción: Los alumnos deben crear un programa que permita al usuario ingresar un texto o número desde el teclado,
# procesarlo (convertirlo a mayúsculas) y mostrarlo en pantalla. Además,
# el programa debe guardar el resultado en un archivo de texto.
# Objetivos: Demostrar cómo se gestionan las operaciones básicas de Entrada y Salida,
# y la interacción con dispositivos de almacenamiento (archivos).

var1 = input()



if isinstance(var1, str):
    var1 = var1.upper()

print(var1)

with open('archivo.txt', 'w') as archivo:
    archivo.write(var1)