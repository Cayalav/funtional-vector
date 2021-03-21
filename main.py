
from random import randrange
from funtions import *

# Tallerarr2- Vectores - Carlos Ayala

 

def num_one(arr):
  print("-------EJERCICIO1-------")
  print("a. Sumatoria: ")
  print(sum(arr))
  print("b. La productoria")
  print(multiply_list(arr))
  print("c. El Mayor Elemento")
  print(max(arr))
  print("d. El menor Elemento")
  print(min(arr))



#Ejercicioarr2
#arr2. De los n elementos de un vector dado calcule:
#a. Cantidad de elementos pares
#b. Cantidad de elementos impares
#c. Cantidad de elementos primos
def num_two(arr):
  print("-------EJERCICIO2-------")

#Ejercicio 3
#3. Dado un Vector arr1 y un Vector v2 de cómo resultado 
#un Vector resultante de las siguientes operaciones:
#a. Suma
#b. Resta
def num_three(arr_one,arr_two):
  print("-------EJERCICIO3-------")

#Ejercicio 4
#4. De los n elementos de un vector dado identifique el número que mas se repite e indique cual es.
def num_four(arr):
  print("-------EJERCICIO4-------")

#Ejercicio 5
#5. Dado un Vect7or arr de longitud par, divida enarr2 partes, en la primera parte realice la productoria y en la segunda la sumatoria. Entregue los valores resultantes.
def num_five(arr): #Validad si es par
  print("-------EJERCICIO5-------")

#Ejercicio 6
#6. Dado un vector arr, indique si es simétrico, un vector es simétrico si siendo longitud par los números de la primera mitad son iguales al inverso de la otra mitad por ejemplo: X=[1arr2,3,3arr2,1], en el ejemplo x es un vector simétrico, en caso que la longitud del vector sea impar, se ignorará el elemento central y se seguirá la misma lógica anterior, por ejemplo: Y=[3,5,7,8,7,5,3], en este ejemplo Y es simétrico.
def num_six(arr):
  print("-------EJERCICIO6-------")

#Ejercicio 7
#7. Dado dos vectores númericos A y B debe realizar las siguiente operaciones con conjuntos:
#a. Unión: Conjunto que contiene(sin repetir) los elementos de A y B.
#b. Intersección: Conjunto que contiene los elementos comunes que aparecen en los conjuntos A y B3
#c. Diferencia(A-B) Conjunto formado por los elementos que pertenecen al conjunto A y no pertenecen al conjunto B.
#d. Diferencia (B-A) Conjunto formado por los elementos que pertenecen al conjunto B y no pertenecel al conjunto A. 
def num_seven(arr_a , arr_b):
  print("-------EJERCICIO7-------")


n = 20  
num_one(random_arr(n))