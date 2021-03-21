from funtions import *

#Vectores - Carlos Ayala

#Inicialización de variables
def print_initial_variables(arr_one, arr_two):
  print("-------VARIABLES INIT-------")
  print("Array #1:")
  print(arr_one)
  print("\n") 
  print("Array #2:")
  print(arr_two)
  print("\n") 
  print("\n") 

# Ejercicio 1
def num_one(arr_one):
  print("-------EJERCICIO1-------")
  print("a. Sumatoria")
  print(sum(arr_one))
  print("b. La productoria")
  print(multiply_list(arr_one))
  print("c. El Mayor Elemento")
  print(max(arr_one))
  print("d. El menor Elemento")
  print(min(arr_one))
  print("\n") 

#Ejercicio 2
def num_two(arr_one):
  print("-------EJERCICIO2-------")
  print("a. Cantidad de elementos pares")
  print(even_arr(arr_one))
  print("b. Cantidad de elementos impares")
  print(odd_arr(arr_one))
  print("c. Cantidad de elementos primos")
  print(prime_arr(arr_one))
  print("\n") 

#Ejercicio 3
def num_three(arr_one, arr_two):
  print("-------EJERCICIO3-------")
  arr_sum = sum_btw_arr(arr_one, arr_two)
  arr_rest = rest_btw_arr(arr_one, arr_two)
  print("a. Suma")
  print(arr_sum)
  print("b. Resta")
  print(arr_rest)
  print("\n")
  
#Ejercicio 4
def num_four(arr_one):
  print("-------EJERCICIO4-------")
  num = most_frequent(arr_one)
  print("a. Elemento más repetido")
  print (num)

#Ejercicio 5
#5. Dado un Vect7or arr_one de longitud par, divida enarr2 partes, en la primera parte realice la productoria y en la segunda la sumatoria. Entregue los valores resultantes.
def num_five(arr_one): #Validad si es par
  print("-------EJERCICIO5-------")

#Ejercicio 6
#6. Dado un vector arr_one, indique si es simétrico, un vector es simétrico si siendo longitud par los números de la primera mitad son iguales al inverso de la otra mitad por ejemplo: X=[1arr2,3,3arr2,1], en el ejemplo x es un vector simétrico, en caso que la longitud del vector sea impar, se ignorará el elemento central y se seguirá la misma lógica anterior, por ejemplo: Y=[3,5,7,8,7,5,3], en este ejemplo Y es simétrico.
def num_six(arr_one):
  print("-------EJERCICIO6-------")

#Ejercicio 7
#7. Dado dos vectores númericos A y B debe realizar las siguiente operaciones con conjuntos:
#a. Unión: Conjunto que contiene(sin repetir) los elementos de A y B.
#b. Intersección: Conjunto que contiene los elementos comunes que aparecen en los conjuntos A y B3
#c. Diferencia(A-B) Conjunto formado por los elementos que pertenecen al conjunto A y no pertenecen al conjunto B.
#d. Diferencia (B-A) Conjunto formado por los elementos que pertenecen al conjunto B y no pertenecel al conjunto A. 
def num_seven(arr_one , arr_two):
  print("-------EJERCICIO7-------")


#Inicialización de los random
n = 20  
arr_one=random_arr(n)
arr_two=random_arr(n)


#Impresión de variables iniciales
print_initial_variables(arr_one, arr_two)


#Resolución de incisos
num_one(arr_one)
num_two(arr_one)
num_three(arr_one, arr_two)
num_four(arr_one)