"""speedy gonzalis """
FINE10 = 10
FINE20 = 20
FINE30 = 30

arrest = ["ryan lee","jake stokes","ethan adams","ben mckowan"]

keep_asking = True
while keep_asking ==True:
    try:
        
        name = (input("what the name there buddy:"))
        limit = int(input("what the speed limit:"))    
        speed = int(input("whats the speed they at:"))    
    except:
        print("that the wrong number boi")
    fast = (speed - limit)  
    if (name in arrest):
        print ("Kill",name,"on site")
        
    if fast >= FINE10:
        print("fine this duuude $80")
            
    elif fast >= FINE20 :
        print("this man costs 130 dollar bills")
        
    elif fast >FINE30:
        print("this man on the hoon charge him $180")
            
    elif fast < FINE10:
        print ("Fine",name,"$30 now and let go")    
       
        
        
