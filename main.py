from funtions import *

#Vectores - Carlos Ayala

#Inicialización de variables
def print_initial_variables(arr_one, arr_two):
  print("-------VARIABLES INIT-------")
  print("Arr1 =",arr_one)
  print("Arr2 =",arr_two)
  print("\n") 

# Ejercicio 1
def num_one(arr_one):
  print("-------EJERCICIO1-------")
  print("a. Sumatoria =",sum(arr_one))
  print("b. La productoria =",multiply_list(arr_one))
  print("c. El Mayor Elemento =",max(arr_one))
  print("d. El menor Elemento =",min(arr_one))
  print("\n") 

#Ejercicio 2
def num_two(arr_one):
  print("-------EJERCICIO2-------")
  print("a. Cantidad de elementos pares =",even_arr(arr_one))
  print("b. Cantidad de elementos impares =",odd_arr(arr_one))
  print("c. Cantidad de elementos primos =",prime_arr(arr_one))
  print("\n") 

#Ejercicio 3
def num_three(arr_one, arr_two):
  print("-------EJERCICIO3-------")
  arr_sum = sum_btw_arr(arr_one, arr_two)
  arr_rest = rest_btw_arr(arr_one, arr_two)
  print("a. Suma =", arr_sum)
  print("b. Rest =", arr_rest)
  print("\n")
  
#Ejercicio 4
def num_four(arr_one):
  print("-------EJERCICIO4-------")
  num = most_frequent(arr_one)
  print("a. Elemento más repetido =", num)
  print("\n")

#Ejercicio 5
def num_five(arr_one): #Validad si es par
  print("-------EJERCICIO5-------")
  if (len(arr_one)%2 == 0):
    arr_prod, arr_sum = split_list(arr_one)
    print("- split 1 =", arr_prod)
    print("- aplit 2 =", arr_sum)
    print("a. La productoria =",multiply_list(arr_prod))
    print("b. Sumatoria =",sum(arr_sum))
  else:
    print("El array no tiene longitud par")
  print("\n")

#Ejercicio 6
def num_six(arr_one):
  arr_two = [1,2,3,4,3,2,1] # Prueba array
  print("-------EJERCICIO6-------")
  if (is_inverse(arr_two)):
    print("El array es simetrico")
  else:
    print("El array no es simetrico")
  arr_two = [1,2,3,4,5,6,7]
  if (is_inverse(arr_two)):
    print("El array es simetrico")
  else:
    print("El array no es simetrico")
    print("\n")

#Ejercicio 7
def num_seven(arr_one , arr_two):
  print("-------EJERCICIO7-------")
  arr_one_set = set(arr_one)
  arr_two_set = set(arr_two)
  print("Unión =", (arr_one_set | arr_two_set))
  print("Intersección =",(arr_one_set & arr_two_set))
  print("A-B =",(arr_one_set - arr_two_set))
  print("B-A =",(arr_two_set - arr_one_set))



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
num_five(arr_one)
num_six(arr_one)
num_seven(arr_one, arr_two)