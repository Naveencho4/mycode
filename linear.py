array=[]

def taking_element():
    
    for i in range(size):
         element = int(input("Enter element "))
         array.append(element)
    return array
flag=0 
size =int(input("enter the size of array"))
array = taking_element()
x=int(input('enter the element to be search in array'))
for i in range(size):

    if (x==array[i]):
        flag=1
        
        break
if (flag==1):
    print('the location is ',i+1)
else:
    print('the element is not find')
