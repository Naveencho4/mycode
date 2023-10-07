x=[1,2,3]
size=int(input("enter the size of array\n"))

print("enter the number of array")
for i in range( size):
    y=int(input(" ss"))
    x.append(y)
print("the number of array are",x)
def sorting():
    for i in range(size - 1):
     for j in range(size - i - 1):
      if x[j] > x[j + 1]:
        x[j], x[j + 1] = x[j + 1], x[j]
sorting()
print("the sorted array is ",x)
print(isinstance(x))
        
   
    