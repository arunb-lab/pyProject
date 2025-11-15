full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
  
    if not isinstance(name, str):
     return "The character name should be a string"

    if len(name)>10:
     return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"

    if (not isinstance(strength, int) or 
        not isinstance(intelligence, int) or 
        not isinstance(charisma, int)):
        return "All stats should be integers"


    if (strength > 4 or intelligence > 4 or charisma > 4):
        return "All stats should be no more than 4"


    return {
        "name": name,
        "strength": strength,
        "intelligence": intelligence,
        "charisma": charisma
    }