#A program that inputs a string or number from the user and determines if it is palindrom or not.
redo="y"
while(redo.lower()=="y"):
    str_num=input("Number or string?(N/S):  ")
#Appending the string charecters to a list using for loop and reversing the list and comparing the both to 
#figure out if its paindrome or not    
    if (str_num.lower()=="s"):
        stri=input("Enter string:  ")
        string_list=[]
        i=0
        for i in stri:
            string_list.append(i)
        reverse_list=string_list[::-1]
        if (reverse_list==string_list):
            print(f"The string {stri} is a palindrome")
        else:
            print(f"the string {stri} is not a palindrome")  
#Basically operating on the number to convert it into reverse using 3 codes and comparing with original
    elif(str_num.lower()=="n"):
         num=int(input("Enter number:  "))
         if(num<0):
             print("Invalid input!")
             continue
         original=num
         reverse=0
         while(num>0):
            remainder=num%10                #1
            reverse=reverse*10+remainder    #2
            num=num//10                     #3 
         if (reverse==original):
            print(f"The number {original} is a palindrome")
         else:
            print(f"The number {original} is not a palindrome")  
    redo=input("Redo?(Y/N):  ")
    print("---------------------------------------------------------------------")



   
    


