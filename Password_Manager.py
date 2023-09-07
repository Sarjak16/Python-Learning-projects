from cryptography.fernet import Fernet

# def write_key():
#     with open ("key.key", "wb") as key_file:
#         key_file.write(key)


def load_key():
    file= open ("key.key", "rb")
    key= file.read()
    file.close()
    return key
        

master_pwd= input("What is the master password? ")
key= load_key()
fer= Fernet(key)
        

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data= line.rstrip()
            user, passw= data.split("|")
            print ("user: ", user, "password:", passw)
            

def add():
    name= input("Account name: ")
    pwd= input("password: ")
    
    with open('password.txt', 'a') as f:
        f.write(name + "|"+pwd + "\n")
    
    
    
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