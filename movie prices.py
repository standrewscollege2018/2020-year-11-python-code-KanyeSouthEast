# age brackets 
AGE_18 = 12
AGE_13 = 9
AGE_5 = 7

# age boundaries
MAX_AGE = 150
MIN_AGE = 0

#input tests
age = int(input("how old are you: "))
student = input("are you a student: ")
if age > MIN_AGE and age < MAX_AGE :
    if student == "yes" :
        print("lucky you your price is $8")
    else :
        if age >= 18 :
            print("the price is $12 ")
        elif age > 13 :
            print("the price is $9")
        elif age > 5 :
            print("the pirce is %7")
        elif age < 5 :
            print("its free entry")
            
            
print("gimme the money")    

