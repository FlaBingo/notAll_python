import random, math
name = input("What's your name: ")
score = int(input("How many rounds do you want to Play(prefer odd no.) : "))
print(f"Best of {score}")
scoreYou, scoreCom = 0,0
for i in range(score):
    
    computer = math.ceil(random.random()*3)
    user = int(input(f"\n{i+1}) Enter 1 --> Rock, 2 --> Paper, 3 --> Scissor :  "))

    if user == 1 and computer == 2:
        if user == 1 and computer == 3:
            print(f"{name} --> Rock\ncomputer --> Scissor \nYou WON")
            scoreYou +=1
        else:
            print(f"{name} --> Rock\ncomputer --> Paper \nYou LOSE")
            scoreCom += 1

    elif user==2 and computer==1:
        if user==2 and computer==3:
            print(f"{name} --> Paper\ncomputer --> Scissor \nYou LOSE")
            scoreCom +=1
        else:
            print(f"{name} --> Paper\ncomputer --> Rock \nYou WON")
            scoreYou += 1

    elif user==3 and computer==1:
        if user==3 and computer==2:
            print(f"{name} --> Scissor\ncomputer --> Paper \nYou WON")
            scoreYou += 1
        else:
            print(f"{name} --> Scissor\ncomputer --> Rock \nYou LOSE")
            scoreCom +=1

    else:
        print("You both chose the same; DRAW")
        

    

print(f"\nTotal Scores\n{name} --> {scoreYou}\nComputer --> {scoreCom}\n\n{"You Won the Game".upper() if scoreCom<scoreYou else "Computer Won the Game".upper() if scoreCom>scoreYou else "You both score the same".upper()}")