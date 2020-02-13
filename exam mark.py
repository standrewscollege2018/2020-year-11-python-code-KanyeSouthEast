
import time

mark = int(input("Please type the mark: "))    
# learn the mark
if mark < 100 and mark >0 :
    if mark >=90 : 
        print("You get an A ")
    # over 90 is an Ae
    
    elif mark >=70 :
        print("You get a B ")
    # over 70 is a B
    
    elif mark >=50 :
        print("You get a C ")
    # over 50 is a C
    elif mark <50 :
        print("You didn't pass ")   
        time.sleep(2.5)
        
        rating = int(input("How difficult was the test out of 10: "))
        if rating >= 7 :
            print("Do you need to try an easier exam")
           
            
        elif rating >=4 :
            print("You are at the right level")
        
        elif rating >=1 :
             print("do you think you should try a harder exam")
        

else :
    print(" Mark is invaid ")


# fail is under 50


#difficulty 