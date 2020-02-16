
#constants 
AGE_BOUNDARY = 12
ADULT_DOSAGE = 500
CHILD_DOSAGE = 10

#weight boundary
MAX_WEIGHT = 150
MIN_WEIGHT = 1

#age boundary
MAX_AGE = 150
MIN_AGE = 0

# inputs
patient_age = int(input("how old are you: "))
patient_weight = int(input("how much do you weigh in kgs: "))

if patient_weight < MAX_WEIGHT and patient_weight > MIN_WEIGHT and patient_age < MAX_AGE and patient_age > MIN_AGE:
    if patient_age >= AGE_BOUNDARY :
        print("Your paracetamol dosage is 2x 500mg tablets")
        
    else :
        print("your recommended paracetamol is ", CHILD_DOSAGE * patient_weight ,"mg") 
# impossible    
else :
    print("This isn't a possible input")
    print(" please try again")
