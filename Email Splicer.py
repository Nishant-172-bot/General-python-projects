#An email splicer function 
#Splits the inputted emailusing split into its designated portions and then printing it also somewhat check email validity
def splicer():
    while True:
        email_input=input("Enter your email address: ")
        if (email_input.find("@")==-1 or email_input.find(".")==-1 ):
            print("Invalid address! ")
            continue
        else:
            (username,domain_full)=email_input.split('@')
            (domain,extension)=domain_full.split('.')
            print(f"Username: {username} ")  
            print(f"Domain name: {domain}")
            print(f"Extension: {extension}")
            option=input("Want to continue?(Y/N): ")
            if (option.lower()=="y"):
                continue
            else:
                break


splicer()

