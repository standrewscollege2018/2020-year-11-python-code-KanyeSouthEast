

# getting information
try:
    auction = input("what ya selling this arvo????")
    bid = int(input("Enter starting bid: "))
    min_bid = int(bid + 1)
    print ("Minnimum bid is:",min_bid)
except:
    #wrong info
    print("Invalid data type use number")
asking = True

while asking == True:
    name = input("Enter your name: ")
    if name == "end":
        asking = False      
    bid = int(input("Enter your bid: "))
    
      
        
    if bid >= min_bid:
        print ("Current bid is:", bid) 
        print(" ")
        print ("and is held by " + name)
        min_bid = (bid + 1)
        print ("New minimum bid is: " ,min_bid)
        print(" ")
    else:
        print("You have the dum-bass, your bid was lower than the minimum try again.")
        
    if asking == False:
        print(name, "won the acution and paid ",bid , "or you get executed")
