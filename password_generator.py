import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    lettters= string.ascii_letters
    digits= string.digits
    special= string.punctuation
    
   characters= letters
   if numbers:
       characters += digits
    if special_characters:
        characters += special
       
    
    
generate_password(8)