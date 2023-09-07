pwd= input("What is the master password? ")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data= line.rstrip()
            user, passw= data.split("|")

def add():
    name= input("Account name: ")
    pwd= input("password: ")
    
    with open('password.txt', 'a') as f:
        f.write(name + "|"+pwd "\n")
    
    
    
while True:
    mode= input("would you like to add a new password or view existing ones(view/ add)?, press Q to quit...").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode. ")
        continue