def first_non_repeating_letter(string):
    count = {}
    for character in string :
        character  = character.lower()
        count.setdefault(character, 0)
        count[character] = count[character] + 1
        
    for character in string :
        if count[character.lower()] == 1:
            return character
    return ''
    #your code here

def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
            
    return ""
