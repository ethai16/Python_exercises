
# for i in range(1,11):
#     print(i)

# value = int(input("What number would you like to start on?"))
# value2 = int(input("What number would you like to end on?"))
# for i in range(value, (value2 + 1)):
#         print(i)


# for i in range(1, 11, 2):
#     print(i)

# for i in range(5):
#     print("*****")

# star = int(input("How big do you want your box?"))
# for i in range(star):
#     print("*" * star)

# width = int(input("Width?"))
# length = int(input("Length?"))

# for i in range(width):
#     if i == 0 or i == width - 1:
#         print("*" * (length + 2))
#     else:
#         print("*" + " " * length + "*")

# height = 10
# for i in range(height):
#     print(" " * (height - i -1)  +  "*" * (2*i+1))

# height = int(input("How tall do you want your tree?"))
# for i in range(height):
#     print(" " * (height - i -1) + "*" * (2 * i + 1))

for i in range(1,11):
    for j in range(1,11):
        print(i ," X " ,j ," = " ,(i * j))