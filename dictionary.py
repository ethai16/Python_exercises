# phonebook_dict = {
#     'Alice': '703-493-1834',
#     'Bob': '857-384-1234',
#     'Elizabeth': '484-584-2923'
# }

# lizNum = phonebook_dict["Elizabeth"]
# phonebook_dict['Kareem'] = ['938-489-2345']
# del phonebook_dict['Alice']
# phonebook_dict['Bob'] = ['968-345-2345']


# print(phonebook_dict)


# ramit = { 
#   'name': 'Ramit', 
#   'email': 'ramit@gmail.com', 
#   'interests': ['movies', 'tennis'], 
#   'friends': [ 
#      { 
#        'name': 'Jasmine', 
#        'email': 'jasmine@yahoo.com', 
#        'interests': ['photography', 'tennis']
#      }, 
#      { 
#         'name': 'Jan', 
#         'email': 'jan@hotmail.com', 
#         'interests': ['movies', 'tv'] 
#      } 
#     ] 
# }

# numRam = ramit['email']
# intRam = ramit['interests'][0]
# adJas = ramit['friends'][0]['email']
# intJas = ramit['friends'][0]['interests'][1]

# print(numRam)
# print(intRam)
# print(adJas)
# print(intJas)


# alphaCount = {
#     'a' : 0,
#     'b' : 0,
#     'c' : 0,
#     'd' : 0,
#     'e' : 0,
#     'f' : 0,
#     'g' : 0,
#     'h' : 0,
#     'i' : 0,
#     'j' : 0,
#     'k' : 0,
#     'l' : 0,
#     'm' : 0,
#     'n' : 0,
#     'o' : 0,
#     'p' : 0,
#     'q' : 0,
#     'r' : 0,
#     's' : 0,
#     't' : 0,
#     'u' : 0,
#     'v' : 0,
#     'w' : 0,
#     'x' : 0,
#     'y' : 0,
#     'z' : 0 
# }

# yourWord = str.lower(input("What word would you like?"))
# def letter_histogram(word):
#     for i in word:
#         if i in alphaCount.keys():
#             alphaCount[i] += 1
#     for key, value in alphaCount.items():
#        if value != 0:
#             print(key, ":" ,value)
#     return alphaCount

# letter_histogram(yourWord)

# wordCount = {
  
# }

# yourParagraph = str.lower(input("Write some words please"))
# splitPara = yourParagraph.split(" ")

# for i in range(len(splitPara)):
#     wordCount[splitPara[i]] = 0
# for i in splitPara:
#     if i in wordCount.keys():
#         wordCount[i] += 1

# print(wordCount)



wordCount = {
  
}

yourParagraph = str.lower(input("Write some words please"))
splitPara = yourParagraph.split(" ")

for i in range(len(splitPara)):
    wordCount[splitPara[i]] = 0
for i in splitPara:
    if i in wordCount.keys():
        wordCount[i] += 1
values = list(wordCount.values())
keys = list(wordCount.keys())

print(keys[0], " : ", values[0])
print(keys[1], " : ", values[1])
print(keys[2], " : ", values[2])




