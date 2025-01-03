#A password generator function
#Storing characters then appending an empty list with a random choice from charecters to generate a passoword of desirable length
import string
import random

def password_generator():
    password_list=[]    
    characters=list(string.ascii_letters + string.digits + "!@#$^%*()")
    option1=input("Want to generate a password?(Y/N): ")
    if option1.lower()=="n":
        return 0
    else:
        while True:
            password_list=[]   
            length=int(input("Length of  your password: "))
            for i in range(length):
                password_list.append(random.choice(characters))
            true_password="".join(password_list)
            print(f"Your password is: {true_password}")
            option2=input("Want to continue?(Y/N): ")
            if option2=='y':
                continue
            else:
                break

password_generator()