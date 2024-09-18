# Ejercicio 2: Simulación de Lectura de Sensores
# Descripción: El segundo programa simulará la lectura de datos de un sensor de temperatura, generando valores aleatorios.
# Estos datos deben procesarse para calcular la temperatura máxima, mínima y promedio.
# Los resultados se mostrarán en pantalla y se guardarán en un archivo de registro.
# Objetivos: Comprender el proceso de lectura y escritura con múltiples lecturas de datos,
# simular un entorno de dispositivos de Entrada/Salida, y la gestión de datos almacenados.

import random


var1 = []

for _ in range(10):
    numeroAleatorio = random.randint(0,50)
    var1.append(numeroAleatorio)




limite = var1.__len__()
suma = 0

menor = 100000
mayor = 0


for i in range(limite):

    suma = suma + var1[i]
    if var1[i] > mayor:
        mayor = var1[i]
    if var1[i] < menor:
        menor = var1[i]


prom = suma / limite

print(var1)
print('la temperatura promedio fue: ', prom)
print('la temperatura mayor fue: ', mayor)
print('la temperatura menor fue: ', menor)

with open('archivo2.txt', 'w') as archivo:
    archivo.write(str(var1) + '\n')  # Convertir la lista var1 a cadena y agregar un salto de línea
    archivo.write('La temperatura promedio fue: ' + str(prom) + '\n')  # Convertir el valor de prom a cadena
    archivo.write('La temperatura mayor fue: ' + str(mayor) + '\n')  # Convertir el valor de mayor a cadena
    archivo.write('La temperatura menor fue: ' + str(menor) + '\n')  # Convertir el valor de menor a cadena





