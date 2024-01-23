print("Welcome to Quitz Game")

#get wish from player
play=input("Do you want to play?")
if play.lower() !="yes":
    quit()
print("Ok Lets Play")

#define score variable
score=0

#define questions
question=input("1.What is the keyword for creating a function in Python?")
if question=="def":
    print("Correct")
    score+=1
else:
    print("Incorrect")
question=input("2.How do you define a constant in Python?")
if question=="None":
    print("Correct")
    score+=1
else:
    print("Incorrect")
question=input("3.What is the method for removing the last element from a list?")
if question=="pop":
    print("Correct")
    score+=1
else:
    print("Incorrect")
question=input("4.What is the operator for exponentiation in Python?")
if question=="**":
    print("Correct")
    score+=1
else:
    print("Incorrect")
question=input("5.How do you check the length of a string or a list?")
if question=="len":
    print("Correct")
    score+=1
else:
    print("Incorrect")
question=input("6.What is the built-in function for finding the maximum value in a list?")
if question=="max":
    print("Correct")
    score+=1
else:
    print("Incorrect")
question=input("7.What is the keyword for creating an empty dictionary?")
if question=="{}":
    print("Correct")
    score+=1
else:
    print("Incorrect")
question=input("8.How do you convert a string to lowercase in Python?")
if question=="lower":
    print("Correct")
    score+=1
else:
    print("Incorrect")
question=input("9.What is the file mode for reading and writing text in Python?")
if question=="r+":
    print("Correct")
    score+=1
else:
    print("Incorrect")
question=input("10.What is the keyword for ending a loop prematurely in Python?")
if question=="break":
    print("Correct")
    score+=1
else:
    print("Incorrect")

#Result
print("Your score is:",score)
