#PROBLEM 1

# with open("file.txt", "r") as f:
#     spcword = f. read()
#     word = "india"
#     if word in spcword:
#         print(f"{word} is present in this file.")
#     else:
#         print(f"{word} is not present in this file.")

# PROBLEM 2
# import random

# def game():
#     print("The game has begin...")
#     newscore = random.randint(1,100)
#     with open("file1.txt", "r") as f1:
#         highScore = (f1.read())
#         if highScore != "":
#             highScore = int(highScore)
#         else:
#             highScore = 0
#     print(f"Your previous score was {highScore}.")

#     with open("file1.txt" , "w") as f2:
#         if highScore<newscore:
#             f2.write(str(newscore))
#         else:
#             f2.write(str(highScore))
#     print(f"Your new Score is {newscore}")
# game()


# PROBLEM 3

# for i in range(2, 21):
#     with open(f"python/tables/table_{i}.txt", "w") as f3:
#         for j in range(1,11):
#             f3.write(f"{i} * {j} = {i*j} \n")
#         f3.write("")
            
# PROBLEM 4

#     word = "Donkey"
#     rep = "######"
#     with open(f"python/tables/table_{i}.txt")as f:
#         oldcontent = f.read()
        
#     newcontent = oldcontent.replace(word, rep)
#     if word in oldcontent:
#         with open(f"python/tables/table_{i}.txt", "w") as f:
#             f.write(newcontent)


# PROBLEM 5

# words = ["stupid", 'dumb', 'idiot', 'moron']
# rep = ['smart', 'sharp', 'intelligent', 'strong']
# oldcontent = ''
# newcontent = ''
# with open("file.txt") as f:
#     oldcontent = f.read()
        
# for i in range(len(words)):
#     oldcontent = oldcontent.replace(words[i], rep[i])
    
    
# with open("file.txt", "w") as f:
#     f.write(oldcontent)
# print(oldcontent)

# PROBLEM 6

# with open("log.txt") as f:
#     content = f.read()

# if "python" in content:
#     print("yes it is present in log.file")
# else:
#     print("no it's not present in log.file")


# PROBLEM 7

# word = "python"
# with open("log.txt") as f:
#     line = f.readlines()
# lineno = 1
# for i in line:
#     if word in line:
#         print(f"yes it's present.")
#     else:
#         print(f"no it's not present.")
            