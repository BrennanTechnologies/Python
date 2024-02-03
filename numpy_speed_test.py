# numpy_speed_test

import numpy as np
import CB_Decorators
import CB_Module as cb

# Create a 1D List
def py_list(x):
	# Create a 1D array
	lst = list(range(x))
	print("list: " + str(lst))
	return lst

# Create a 1D array
def np_array(x):
	arr = np.arange(x)
	print("np_array: " + str(arr))
	return arr

x = 10
lst = py_list(x)
arr = np_array(x)

sum = 0
for i in lst:
	my_sum = sum + i
	print(i)
print("Sum: " + str(my_sum))


# @timer
# def test():
# 	pass
