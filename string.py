# sentence = str.upper(input("Sentence please"))
# print(sentence)

# cap = (input("Sentence please again"))
# capital = cap.capitalize()
# print(capital)

# string = str(input("Sentence please again again"))
# reverse = string[::-1]
# print(reverse)

# newList = []
# para = list(str.upper(input("Type a paragraph")))
# for i in para:
#     if i == "a":
#         i = "4"
#     elif i == "E":
#         i = "3"
#     elif i == "G":
#         i = "6"
#     elif i == "I":
#         i = "1"
#     elif i == "O":
#         i = "0"
#     elif i == "S":
#         i = "5"
#     elif i == "T":
#         i = "7"
    
#     newlist.append(i)
   


# print(" ".join(newlist))

word = str.lower(input("Long vowel word?"))
oldList = []


for x in word:
    oldList.append(x)
for i in range(len(word)):
    if word[i-1] == "o" and word[i] == word[i-1]:
        oldList[i] = "oooo"
    elif word[i-1] == "e" and word[i] == word[i-1]:
        oldList[i] = "eeee"

newString = " ".join(oldList)
withOutspace = newString.replace(" ","")
print(withOutspace)


