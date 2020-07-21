sentence = input("You sentence: ")

length = len(sentence)
section = sentence[2:6]
first = sentence.split(' ')
cap = str.capitalize(sentence)

print(length)
print(section)
print(first[0]*3)
print(cap)
