#List Exercise

# numbers = [5,4,6,7,8]
# sum = 0
# for number in numbers:
#     sum += number
# print(sum)

# numbers = [5,10,300,450,509,1,3,4, -3, -7, -10, -12]
# numbers.sort()
# length = len(numbers)
# print("Largest number:", numbers[length - 1])
# print("Smallest number:", numbers[0])

# even = []
# odd = []

# for i in numbers:
#     if i % 2 == 0:
#         even.append(i) 
#     else:
#         odd.append(i)

# print("Even numbers: ", even)
# print("Odd numbers: ", odd)

# for i in numbers:
#     if i > 0:
#         print(i)

# positive = []
# negative = []

# for i in numbers:
#     if i > 0:
#         positive.append(i)
#     else:
#         negative.append(i)

# print(positive)
# print(negative)

# factor = 3
# finalProducts = []

# for number in numbers:
#     product = factor * number
#     finalProducts.append(product)

# print(finalProducts)

# numberList1 = [2,5,4]
# numberList2 = [5,6,7]
# numberList3 = []
# for i in numberList1:
#     x = numberList1.index(i)
#     numberList3.append(numberList1[x] * numberList2[x])

# print(numberList3)

twoDim1 = [[2, -2], [5,3]]
twoDim2 = [[3, -3], [-6,3]]
result = [[0,0], [0,0]]

for i in range(len(twoDim1)):
    for j in range(len(twoDim1[0])):
        result[i][j] = twoDim1[i][j] + twoDim2[i][j]
for r in result:
    print(r)


