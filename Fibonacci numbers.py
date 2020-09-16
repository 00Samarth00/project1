
def fn_(n1,n2):
    return n1+n2

x=eval(input('ENTER THE NO. OF FIBONACCI NUMBERS YOU WANT TO SEE:'))

fns=[0,1]
for i in range(0,x-2):
    
    fns.append(fn_(fns[-2],fns[-1]))
               
    

print('LIST OF',x,'FIBONACCI NUMBERS :-',fns)
