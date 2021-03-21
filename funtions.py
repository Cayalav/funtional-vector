import numpy as np

def multiply_list(my_list) :
  result = 1
  for x in my_list:
       result = result * x 
  return result 

def random_arr(n) :
  return np.random.rand(n) 