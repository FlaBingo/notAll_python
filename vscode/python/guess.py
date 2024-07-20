import random, math

randomnum = math.ceil(random.random()*100)
# print(randomnum)

while True:
    print()
    ask = int(input("Guess the number: "))
    if randomnum == ask:
        print(f"Correct, It was {randomnum}")
        break
    elif randomnum < ask and randomnum > 0:
        print(f"Answer is small")
    elif randomnum > ask and randomnum < 101:
        print(f"Answer is big")
    else:
        print(f"{ask} is invalid, your number should be between 1 and 100")
    
    
        