print("welcome to the computer quiz")
playing= input("Do you want to play? ")
print(playing)

if playing != "yes":
    quit()
print("okay! lets start the game :)")

answer = input(" What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct answer!!!!!!!!")
else:
    print("Invalid answer!!!!")
    