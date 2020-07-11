word = input()
# if word.islower():
#     print(word)

for letter in word:
    if letter.isupper():
        word = word.replace(letter, "_" + letter.lower())

print(word)
