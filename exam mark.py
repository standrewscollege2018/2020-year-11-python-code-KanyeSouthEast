
import time
#mark grade boundaries
A_GRADE_BOUNDARY = 90 
B_GRADE_BOUNDARY = 70
C_GRADE_BOUNDARY = 50

# max and min mark
MAX_GRADE = 100
MIN_GRADE = 0


mark = int(input("Please type the mark: "))    
# learn the mark


if mark < MAX_GRADE and mark > MIN_GRADE :
    if mark >= A_GRADE_BOUNDARY: 
        print("You get an A ")
    # over 90 is an A
    
    elif mark >= B_GRADE_BOUNDARY :
        print("You get a B ")
    # over 70 is a B
    
    elif mark >=C_GRADE_BOUNDARY :
        print("You get a C ")
    # over 50 is a C
    elif mark <C_GRADE_BOUNDARY :
        print("You didn't pass ")   
        time.sleep(2.5)
        
        rating = int(input("How difficult was the test out of 10: "))
        if rating >= 7 :
            print("Do you need to try an easier exam")
           
            
        elif rating >=4 :
            print("You are at the right level")
        
        elif rating >=1 :
             print("do you think you should try a harder exam")
        # difficulty

else :
    print(" Mark is invaid ")


