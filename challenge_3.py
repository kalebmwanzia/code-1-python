def highest_consonant_value(s):
    def get_consonant_value(letter):
        consonants = 'bcdfghjklmnpqrstvwxyz'
        return ord(letter) - ord('a') + 1 if letter in consonants else 0

    max_value = 0
    current_value = 0

    for char in s:
        if char in 'aeiou':
            max_value = max(max_value, current_value)
            current_value = 0
        else:
            current_value += get_consonant_value(char)

    max_value = max(max_value, current_value)
    return max_value


input_string = "y"
result = highest_consonant_value(input_string)
print("Highest value of consonant substrings:", result)