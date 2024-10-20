vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = set() # cria um conjunto vazio

for letter in word:
    if letter in vowels:
        found.add(letter)

print(found)
