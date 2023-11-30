print("Welcome to my computer quiz!")

playing = input("Do you want to play a programming quiz game? ")

if playing.lower() != "yes":
    quit()

score=0

print("Okay! Let's play :) ")
answer = input("What is the most popular programming problem? ")
if answer.lower() == "missing a semicolon":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
   
answer = input("Why is Python slow? ")
if answer.lower() == "because of idle":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("What two words every programmer learned to code first? ")
if answer.lower() == "hello world":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("What is the golden rule in programming? ")
if answer.lower() == "if it works, don't touch it":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("Can you give me a programming music note? ")
if answer.lower() == "c#":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 5)*100) + " %.")

    
