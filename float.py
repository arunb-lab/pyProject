#How Do You Work With Integers and Floating Point Numbers?
#In Python, integers and floating point numbers are two of the most commonly used numeric data types. Here's how you can work with them:
#Creating Integers and Floating Point Numbers
#You can create integers and floating point numbers simply by assigning values to variables.
#Integer
int_num = 10
#Floating Point
float_num = 10.5    
print(f"Integer: {int_num}, Floating Point: {float_num}")
#Basic Arithmetic Operations
a = 15
b = 4
#Addition   
add = a + b
#Subtraction
sub = a - b
#Multiplication
mul = a * b
#Division
div = a / b
#Floor Division
floor_div = a // b
#Modulus
mod = a % b
#Exponentiation
exp = a ** b
print(f"Addition: {add}, Subtraction: {sub}, Multiplication: {mul}, Division: {div}, Floor Division: {floor_div}, Modulus: {mod}, Ex
ponentiation: {exp}")
#Type Conversion
#Convert Integer to Float
int_to_float = float(int_num)
#Convert Float to Integer
float_to_int = int(float_num)
print(f"Integer to Float: {int_to_float}, Float to Integer: {float_to_int}")
#Using Built-in Functions
#Absolute Value
abs_val = abs(-20)
#Power
power_val = pow(2, 3)
#Round
round_val = round(10.567, 2)
print(f"Absolute Value: {abs_val}, Power: {power_val}, Round: {round_val}")
#Working with Large Integers
large_int = 123456789012345678901234567890
print(f"Large Integer: {large_int}")
#Using the math Module
import math
#Square Root
sqrt_val = math.sqrt(16)
#Ceiling
ceil_val = math.ceil(10.2)
#Floor
floor_val = math.floor(10.8)
print(f"Square Root: {sqrt_val}, Ceiling: {ceil_val}, Floor: {floor_val}")
#Conclusion
#Integers and floating point numbers are fundamental data types in Python that allow you to perform a
#wide range of mathematical operations. By understanding how to create, manipulate, and utilize these types, you can effectively handle numerical data in your Python programs.
#Remember to always consider the precision and limitations of floating point arithmetic when working with decimal numbers.
#Example of precision issue with floating point
a = 0.1 + 0.2
print(f"0.1 + 0.2 = {a} (Expected: 0.3)")
#To mitigate precision issues, consider using the decimal module for high-precision arithmetic
from decimal import Decimal
a = Decimal('0.1') + Decimal('0.2')
print(f"Using Decimal: 0.1 + 0.2 = {a}
    (Expected: 0.3)")
#This code demonstrates how to work with integers and floating point numbers in Python, including creation, arithmetic operations, type conversion, and handling precision issues.
