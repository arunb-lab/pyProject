numbers = [1, 2, 3, 4, 5]

square = lambda x: x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]
## Using lambda directly in map
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]  
# Using lambda with filter to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # [2, 4]                        
# Using lambda with reduce to get the product of all numbers
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product) # 120
# Using lambda with sorted to sort a list of tuples based on the second element
tuples_list = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_list = sorted(tuples_list, key=lambda x: x[1])
print(sorted_list) # [(2, 'a'), (1, 'b'), (3, 'c')]
# Using lambda with max to find the longest string in a list
strings = ['apple', 'banana', 'cherry', 'date']
longest_string = max(strings, key=lambda x: len(x))
print(longest_string) # 'banana'
# Using lambda with min to find the tuple with the smallest second element      
tuples_list = [(1, 3), (2, 1), (3, 2)]
smallest_tuple = min(tuples_list, key=lambda x: x[1])
print(smallest_tuple) # (2, 1)  
# Using lambda with map to convert temperatures from Celsius to Fahrenheit
celsius_temps = [0, 20, 37, 100]
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print(fahrenheit_temps) # [32.0, 68.0, 98.6, 212.0]
# Using lambda with filter to get strings that start with 'a'
words = ['apple', 'banana', 'avocado', 'cherry', 'apricot']
a_words = list(filter(lambda word: word.startswith('a'), words))
print(a_words) # ['apple', 'avocado', 'apricot']
# Using lambda with reduce to concatenate a list of strings
strings = ['Hello', ' ', 'World', '!']
concatenated_string = reduce(lambda x, y: x + y, strings)
print(concatenated_string) # 'Hello World!'