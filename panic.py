phrase = "Don't panic!"
plist = list(phrase)
print(phrase)

plist.remove('D')
plist.remove("'")
plist.pop(3)

while len(plist) > 5:
    plist.pop()

print(plist)

plist.insert(2, ' ')
plist.insert(4, plist.pop(5))

print(plist)

manipulated_phrase = ''.join(plist)
print(manipulated_phrase)

# new_phrase = ''.join(plist)
# print(plist)
# print(new_phrase)