#Importing Math Module
import math

#Taking 2 numbers as input by type casting to floating from string datatype
x = float(input ("Enter a number, x = "))
y = float(input ("Enter a number, y = "))

#Printing results by string concatenate and string type casting
print ("Number 'x', raised to the power 'y'= " + str(pow(x, y)))
print ("The log (base 2) of 'x'= " + str("{:.2f}".format(math.log2(x))))