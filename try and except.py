"""how to use try-except for error handling"""
try:
    age = int(input("enter your age: "))
    print(age)

except:
    print("error you suck")

keep_asking = True

    
while keep_asking == True:
    try:
        value = int(input("enter thy number kook:"))
        keep_asking = False
    except:
        print("error you suck grom")
        
print("you number is stupid" , value)