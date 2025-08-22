def countdown(count):
    if count <= 0:
        print("please provide the possitive no only")
    else:       
        print(f"starting {count} -second countdown")
        while count>0:
            print(count)
            count-=1
        print("Blast off!")   

countdown(0)     

