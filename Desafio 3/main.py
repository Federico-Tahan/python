from Funciones import *

v = vector_unknown_range(300000)

def total_elements(v):
    count = 0
    for element in v:
        count += 1
    return count

print("The total number of elements in the list: ", total_elements(v))