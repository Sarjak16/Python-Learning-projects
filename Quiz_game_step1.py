print("welcome to the computer quiz")
playing= input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()
print("okay! lets start the game :)")

answer = input(" What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct answer!!!!!!!!")
else:
    print("Invalid answer!!!!")
    
answer = input("fullform of GPU is? ").lower()
if answer == "graphics processing unit":
    print("Correct answer!!!!!!!!")
else:
    print("Invalid answer!!!!")
    
    
    answer = input(" What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct answer!!!!!!!!")
else:
    print("Invalid answer!!!!")
    
    
    answer = input(" what does PSU stand for? ").lower()
if answer == "power supply":
    print("Correct answer!!!!!!!!")
else:
    print("Invalid answer!!!!")
    
    