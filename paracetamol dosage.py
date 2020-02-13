
AGE_BOUNDARY = 12
ADULT_DOSAGE = 500
CHILD_DOSAGE = 10

patient_age = int(input("how old are you: "))
patient_weight = int(input("how much do you weigh in kgs: "))

if patient_age >= AGE_BOUNDARY :
    print("Your paracetamol dosage is 500mg")
    
else :
    print("your recommended paracetamol is", CHILD_DOSAGE*patient_weight ,"mg") 


