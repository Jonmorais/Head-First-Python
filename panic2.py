phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

word_on = ''.join(plist[1:3])
on_tap = word_on + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(on_tap)