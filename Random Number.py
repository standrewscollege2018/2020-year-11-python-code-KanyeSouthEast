import random

keep_asking = True
num = random.randint(1,100)

try:
    while keep_asking == True:
        numb = int(input("enter a number between 1-100: "))
           
        if numb == num:
            print("correct you are")
            print("celebrate good times come on")
            keep_asking = False
        else:
    
            if num > numb:
                print("higher")
            else:
                print("lower")
            
except:
    print("incorect value")
    
    
