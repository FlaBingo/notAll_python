# TEXT TO SPEECH
    # import pyttsx3
    # engine = pyttsx3.init()
    # engine.say("")
    # engine.runAndWait()
    
# CHECK FILES
    # import os
    # directory = "/"
    # items = os.listdir(directory)
    # for item in items:
    #     print(item)
    
# ADD TWO NUMBERS
# add = lambda a,b : a+b
# print(add(6 ,20))

# AVERAGE OF GIVEN NUMBERS
# numbers = (input("Enter the numbers you want get the avg of (separated by space): "))
# listnum = numbers.split()
# print(listnum)
# add = 0 
# for i in range(len(listnum)):
#     add += int(listnum[i])
# result = add/len(listnum)
# print(f"Avg value of given numbers is: '{result}'")
    
# somewords = "Hello my name  is  satyam  and I am a good boy"
# print(somewords.replace("  "," "))

# BASIC TRANSLATER(HINDI TO ENGLISH)
# trans = {"namaste" : "Hello", "dunia":"World", "achhaa": "good",'madad':'Help',"billi":"Cat","kutta":"Dog","bhagvan":"God","kursi":"Chair"}
# toEng = input("Enter something you want to translate: ")
# print(trans[toEng])

# # FACTORIAL
# def factorial(num):
#     result = num
#     if num>0 :
#         for i in range(1, num):
#             result = result * (num - i)
#         return f"The factorial of {num} is {result}"
#     else:
#         return "Invalid number"
    
# num = int(input("Enter the number: ")) 
# print(factorial(num))


# n = int(input("Enter a number: "))
# PYRAMID PATTERN
# for i in range(1,a+1):
#     print(" " * (a-i), end="")
#     print("*"* (2 * i - 1), end="")
#     print()

# PATTERN
# for i in range(1, n+1):
#     # print("*"*i)
#     if i == 1 or i ==(n):
#         print("* "*(n), end="")
#         print()
#     else:
#         print("*", end="")
#         print(" "*(n*2-3), end="")
#         print("* ")


# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{n} * {11-i} = {n*(11-i)}")




# FAHRENHEIT TO CELCIUS
# def FtoC(F):
#     C = (F - 32)*(5/9)
#     return round(C, 2)

# CELCIUS TO FAHRENHEIT
# def CtoF(C):
#     F = (C*(9/5))+(32)
#     return round(F, 2)

# print(CtoF(5/9))


# n = int(input("Enter a number: "))
# # for i in range(1,n+1):
# #     print("* "*((n+1) - i))

# # BY RECURSION
# # def pattern(n):
# #     if n == 0:
# #         return
# #     print("* "*n)
# #     pattern(n-1)

# # pattern(n)
# print(n)





list = ["vedant", "atharva", "akshay", "siddhesh","satyam"]
word = "atyhm"
def rm(list,word):
    n = []
    for item in list:
        if True:
            n.append(item.strip(word))
    return n
print(rm(list,word))