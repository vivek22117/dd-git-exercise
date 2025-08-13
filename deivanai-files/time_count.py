
def countdown(cound):
    if cound <= 0:
        print("Plese give the postive numbers")
    else:      
        print("Starting {} second countdown:".format(cound))
        while cound > 0:
         print(cound)
         cound -= 1
        print("Blast off") 

countdown(0)   
        

   

