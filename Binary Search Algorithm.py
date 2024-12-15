#Binary Search Algorithm
#Basically need to cut down the list with the while loop until the target is met

import random

def search_function(list, target):
    start=0
    end=len(list)
    middle=0
    steps=1
    while (start!=end):
        middle=(end+start)//2
        print("Step",steps,":", "[",start,"-",end,"]")
        if target==middle:
            return middle
        elif target<middle:
            end=middle
        elif target==start:
            return start
        elif target==end:  
            return end  
        else:
            start=middle  
        steps +=1  

#The Main Function:
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,6,17,18,19,20]
rand_target=random.choice(list)
print(f"The given list is:",list)
print(f"The randomized target of the list is:",rand_target)
print(f"The number found was:",search_function(list,rand_target))
  



