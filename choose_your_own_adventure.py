name= input("Type your name: ")
print(" We welcome", name, "to  the adventure game world. ")

answer= input("you are on a dirt road, it has come to an end you can go either to left or right. which way would you like to go? ").lower()
if answer=="left":
    answer= input("you come ro a river, you like to walk around it or swim across?, type walk to walk around and swim to swim across: ").lower()
    
    if answer=="swim":
        print("you swam and you were eaten by an aligator. ")
    elif answer=="walk":
        print("you walk for a miles and you ran out of the water and you died")
    else:
        print("Not a valid option.....You loose!!!")
                          
elif answer=="right":
    input("you come ro a bridge , it looks wobbly , do you want to cross it or head back (cross/ back)? ").lower()
    
    if answer=="back":
        print("you go back to the main road and ypu didnt reach to destination. you loose!!!!!!!!  ")
    elif answer=="cross":
        answer= input("you cross the bridge and met a stranger . Do you talk to him (yes/ no)? ")
        if answer== "yes":
            print("you talked to stranger and he gave you the gold you were trying to find. you Win!!!!!!!! ")
        elif answer== "no":
            print("you ignored the stranger, you didnt reach to gold he had and you loose!!!!!!!")
        
        else:
            print("not a valid option you loose!!!!")
              
    else:
        print("Not a valid option.....You loose!!!")
else:
    print("not a valid answer, you loose!!!")