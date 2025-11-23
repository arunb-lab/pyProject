def pin_extractor(poem):
    secret_code = ''
    lines = poem.split("\n") #plit the lines on the newline character (\n), and assign the resulting list to a variable called lines.

    for line_index, line in enumerate(lines):
        print(line_index, line)  # Print each line to the console.
        words = line.split() # Split each line into words based on spaces, and assign the resulting list to a variable called words.
        print(words)  # Print the list of words to the console.
        if line_index < len(words):
            print(words[line_index])  # Print the word at the position corresponding to the line index.
        else:
            pass
    return secret_code
    
poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)

#nothig today beacuse it's saturday this isfor github streak
#nothig today beacuse it's saturday this isfor github streak

#freecodecamp.py
def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text