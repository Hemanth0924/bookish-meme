import random

response = input("Do you want to roll a dice?")
print("\n") 
#y = "Yes" or "yes"

while response == "y":
    no = random.randint(1,6)

    #Condition to check the number value

    if no == 1:
        print("[------]")
        print("[------]")
        print("[   0  ]")
        print("[------]")
        print("[------]")

    if no == 2:
        print("[-----]") 
        print("[ 0   ]") 
        print("[     ]") 
        print("[   0 ]") 
        print("[-----]") 
    
    if no == 3:
        print("[-----]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[-----]")  
    
    if no == 4:
        print("[-----]") 
        print("[0   0]") 
        print("[     ]") 
        print("[0   0]") 
        print("[-----]") 
    
    if no == 5:
        print("[-----]") 
        print("[0   0]") 
        print("[  0  ]") 
        print("[0   0]") 
        print("[-----]") 
        
    if no == 6:
        print("[-----]") 
        print("[ 0 0 ]") 
        print("[ 0 0 ]") 
        print("[ 0 0 ]") 
        print("[-----]") 


