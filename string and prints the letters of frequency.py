def countChars (string):
    chars = {}
    for char in string :
        if char in chars :
            chars [char] += 1
        else:
            chars[char] = 1
    return chars

string = input(" Enter a string : ")
chars = countChars(string)
for char , count in countChars (string).items():
    print(f"{char}: 0{count}")
