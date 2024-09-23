import random



print('en este juego tienes que adivinar un numero del 1 al 6')

num = int(input('Ingrese el numero '))

array = []


for i in range(1):
    array.append(random.randint(1,6))

print(array)

if num in array:
    print('Adivinaste')
else:
    print('sigue intentando')


var1 = 'manu'

var2 = 'rivas'

print(var1+var2)