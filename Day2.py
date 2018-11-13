# name = input("What is your name?")
# print("Hello," + name + "!")


# name = input("WHAT IS YOUR NAME?")
# name = name.upper()
# nameLen = len(name)
# string = "Hello, %s! Your name has %d letters in it!" %(name, nameLen)
# upperString = string.upper()
# print(upperString)


# madlib = "Please fill in the blanks below: My favorite basketball team is ___(team)___, but my favorite player is ___(player)___!"
# print(madlib)
# team = input("What is team?")
# player = input("What is player?")
# finishedMadlib = "My favorite basketball team is %s, but my favorite player is %s" %(team, player)
# print(finishedMadlib)

# day = int(input('Day (0-6)?'))
# if day == 0:
#     print('Sunday')
# elif day == 1:
#     print('Monday')
# elif day == 2:
#     print('Tuesday')
# elif day == 3:
#     print('Wednesday')
# elif day == 4:
#     print('Thursday')
# elif day == 5:
#     print('Friday')
# elif day == 6:
#     print('Saturday')
# else:
#     print('Invalid response')

# day = int(input('Day (0-6)?'))
# if day == 0 or day == 6:
#     print('Sleep in')
# elif day >= 1 and day <= 5 :
#     print('Go to work')
# else:
#     print('Invalid response')


# celcius = int(input("Temperature in C?"))
# convertF = celcius * 1.8 + 32
# print(str(convertF) + "F")


# billAmount = int(input("The total bill amount: "))
# service = input("The level of service, which can be one of the following: good, fair, or bad ")
# lowerService = service.lower()
# tipAmount = 0
# if lowerService == "good":
#     tipAmount = .20 * billAmount
# elif lowerService == "fair":
#     tipAmount = .15 * billAmount
# elif lowerService == "bad":
#     tipAmount = .10 * billAmount
# else:
#     print("Invalid Response")
# totalBill = tipAmount + billAmount
# print("Tip Amount: ${:.2f}".format(tipAmount))
# print("Total Amount: ${:.2f}".format(totalBill))


# billAmount = int(input("The total bill amount: "))
# service = input("The level of service, which can be one of the following: good, fair, or bad ")
# split = int(input("Split how many ways? "))
# lowerService = service.lower()
# tipAmount = 0
# if lowerService == "good":
#     tipAmount = .20 * billAmount
# elif lowerService == "fair":
#     tipAmount = .15 * billAmount
# elif lowerService == "bad":
#     tipAmount = .10 * billAmount
# else:
#     print("Invalid Response")
# totalBill = tipAmount + billAmount
# perPerson = totalBill / split
# print("Tip Amount: ${:.2f}".format(tipAmount))
# print("Total Amount: ${:.2f}".format(totalBill))
# print("Amount per person: ${:.2f}".format(perPerson))


# count = 0
# while count < 10:
#     count += 1
#     print(count)


coinAmount = 0
print("You have 0 coins.")

anotherCoin = str.lower(input("Do you want another?" ))

while anotherCoin == "yes":
    coinAmount += 1
    print("You have %d coins" %(coinAmount))
    anotherCoin = str.lower(input("Do you want another?" ))

if anotherCoin == "no":
    print("Bye")
else:
    print("invalid")

















