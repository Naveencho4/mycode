import random
import string
code=str(input("enter the message\n"))
lenght=(len(code))
message=code
print("\nencrepeted")
   
if(lenght<3):
    message=message[::-1]
    print(message)
else:
    codending=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase,k=3))
    codestart=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase,k=3))
    startingword=message[0]
    remaning_message=message[1:]
    print(codestart+remaning_message+startingword+codending)

print("\ndecrepeted")

if(lenght<3):
    message=message[::-1]
    print(message)
else:
    message =(message[3:-3]) 
    startingword=message[::-1]
    remaning_message=message[::-1]
    message=startingword+ remaning_message
    print(code)

