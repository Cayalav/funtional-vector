import numpy as np

def random_arr(n): #Generador Array
  return np.random.randint(15, size=n) 

def multiply_list(arr): #Productoria
  result = 1
  for x in arr:
    result = result * x 
  return result 

def even_arr(arr): #Pares
  count=0
  for x in arr:
    if (arr[x]%2==0):
      count+=1
  return count 
  
def odd_arr(arr): #Impares con negación
  count=0
  for x in arr:
    if (not arr[x]%2==0):
      count+=1
  return count 

def prime_arr(num):
    count=0
    for n in num:
      if n>1:
         for i in range(2,n):
            if (n%i)==0:
                break
            else:
                count+=1
    return count