full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
  
    if not isinstance(name, str):
     return "The character name should be a string."

    if len(name)>10:
        return "the character name is  too long"
    if " " in name:
        return "The character name should not contain spaces"

    return {
        "name": name,
        "strength": strength,
        "intelligence": intelligence,
        "charisma": charisma
    }