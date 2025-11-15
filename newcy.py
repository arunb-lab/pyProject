t = str.maketrans('lk', 'br')
sentence = 'The tent gave in to the leaks.'

print(sentence.translate(t))
# Output: The tent gave in to the bears.