name= input("Type your name")
print("welcome", name, "to  the adventure game world")

answer= input("you are on a dirt road, it has come to an end you can go either to left or right. which way would you like to go? ").lower()
if answer=="left":
    answer= input("you come ro a river, you like to walk around it or swim across?, type walk to walk around and swim to swim across: ").lower()
    
    if answer=="swim":
        print()
    elif answer=="walk":
        print()
    else:
        print("Not a valid option.....You loose!!!"
elif answer=="right":
    print()
else:
    print("not a valid answer, you loose!!!")