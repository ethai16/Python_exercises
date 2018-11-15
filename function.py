# def hello(name):
#     print("Hello " + name)
# hello("Erick")

import matplotlib.pyplot as plot

# def f(x):
#     return x + 1
# xs = list(range(-3,4))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot(xs,ys)
# plot.show()

# def f(a, b, c):
#     return (a*x**2 + b*x + c)

# xs = list(range(-100,101))
# ys = []

# for x in xs:
#     ys.append(f(1,0,0))

# plot.plot(xs,ys)
# plot.show()

# def f(x):
#     if x % 2 == 0:
#         return -1
#     else:
#         return 1

# xs = list(range(-5,5))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.bar(xs,ys)
# plot.show()

import math

# def f(x):
#     return math.sin(x)
# xs = list(range(-5,5))
# ys = []

# for x in xs:
#     ys.append(f(x))
# plot.plot(xs,ys)
# plot.show()

from numpy import arange

# def f(x):
#     return math.sin(x)

# xs = arange(-5, 5, 0.1)
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot(xs,ys)
# plot.show()

# def f(x):
#     return x * 1.8 + 32
# xs = list(range(-100,101))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot(xs,ys)
# plot.show()

# play = str.upper(input("Do you want to play again(Y/N)"))

# def quest(play):
#     if play == "Y":
#         return True
#     else:
#         return False
# print(quest(play))

play = str.upper(input("Do you want to play again(Y/N)"))

def quest(play):
    while play == "Y":
        value = True
        play = str.upper(input("Do you want to play again(Y/N)"))
    if play == "N":
        return False
    else:
        print("Invalid Response!")
        play = str.upper(input("Do you want to play again(Y/N)"))

        
print(quest(play))


