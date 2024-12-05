from array import array


array1 = array('i', [1, 2, 3])  
array2 = array('i', [4, 5, 6])  

appended_array = array('i', array1 + array2)

print("Appended Array: ", appended_array)
