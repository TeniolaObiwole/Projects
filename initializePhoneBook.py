import json
phonebook = {}
#json.dump(phonebook, open('phoneBook.txt','w'))

p = json.load(open('phoneBook.txt'))
print(type(p))
print(p)