string = input("Enter the string: ")
duplicates = set()
updated_string = ""

for char in string:
    if char != ' ' and string.count(char) > 1 and char not in duplicates:
        duplicates.add(char)
    if char in duplicates:
        updated_char = chr(ord(char) + 1) if char != 'z' else 'a'
        updated_string += updated_char
    else:
        updated_string += char

print("Original string: ", string)
print("Duplicate string: ", duplicates)
print("Updated string: ", updated_string)
