#Tutorial followed with TechWithTim YouTube 7 Jan 2022#

#Welcome statement#
print("Welcome to the Game!")

#Request to play#
playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Let's begin!")
score = 0

answer = input("What does 2 + 2 equal? ")
if answer == "4":   
    print("Correct!")
    score += 1
else:
    print("Simple addition. Incorrect.")


answer = input("What does a bird fly with? ")
if answer.lower() == "wings":   
    print("Correct!")
    score += 1
else:
    print("Simple anatomy. Incorrect.")

answer = input("What color is the sky? ")
if answer.lower() == "blue":
    print("Correct!")
    score += 1
else:
    print("Simple color. Incorrect.")

answer = input("What planet do you live on? ")
if answer.lower() == "earth":
    print("Correct!")
    score += 1
else:
    print("Simple name. Incorrect.")

print("You got " + str(score) + " questions correct!")
print("Percentage correct " + str((score/4) * 100) + "%.")