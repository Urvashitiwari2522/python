# how importing in python works
# Importing in python is the process of loading code  from python module into the current script
# This allows you to used the functions and variables defined in the module in your current script.
# import pandas 
# pandas.read_csv() 
import math
result = math.sqrt(9)
print(result)

'''From keyword->
You can also import specific function or variables from a module  using the from keyword'''
from math import sqrt,pi
print(math.sqrt(25)*pi)

''' importing everything 
it also possible to import all the variables and functions from a module using * wildcart
'''
# from math import *
''' as Keyword
python also allows you to rename the import modules using as keyword
this can be usefull if you can use a short and more descriptive name for a import module'''    
import math as m
print(m.floor(6.4332))

'''The dir function
finally, python as a built-in-function c/d dir that you can used to view the name of all the 
functions and variables define in the module. 
This can be useful for exploring and understanding the content of the new module.'''
import math
print(dir(math))

from function import *
