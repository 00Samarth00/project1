#TASK:-1,AREA OF CIRCLE

while(True):
    print('To calculate the area of circle:')
    r=eval(input("Enter the value of its Radius="))

    if(type(r)==int or type(r)==float):
        print("Area of circle of given radius=",3.14*(r**2))

    else:
        print("PLEASE ENTER VALID VALUE FOR RADIUS")
        
    
    c=input("DO YOU WANT TO FIND OUT AREA OF ANOTHER CIRCLE? (y/n)").casefold()
    if(c=='y' or c=='yes'):
            continue
    elif(c=='n' or c=='no'):
            print('SEE YOU AGAIN.BYE!!')
            break
    else:
        print('PLEASE ENTER "YES" OR "NO"')

#TASK:-2,EXTENSION OF FILE
    
print('To know the extension of a file:-')
while(True):
    name=input("ENTER THE NAME OF FILE:")
    ext=name.split(".")

    if(len(ext)>=2):
        print('EXTENSION OF THE GIVEN FILE IS:',repr(ext[-1]))
        break
    else:
        print('ENTER VALID FILE NAME!!!')
        continue
    


  
        
   
    
    
        
    

