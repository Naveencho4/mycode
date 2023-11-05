import random
import string

message=str(input("enter the message\n"))

def encrepeted():
    print("\nencrepeted")
    lenght=(len(message))
    if(lenght<3):
        message=message[::-1]
        print(message)
    else:
        codending=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase,k=3))
        codestart=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase,k=3))
        startingword=message[0]
        trying2=message.replace(message[0],"")
        message=trying2+startingword
    
        print(codestart+message+codending)
def decrepeted():
    print("\ndecrepeted")
    lenght=(len(message))
    if(lenght<3):
        message=message[::-1]
        print(message)
    else:
        message = ''.join(message[3:-3]) 
        print(message)
        startingword=message[-1]
        trying2=message.replace(message[-1],"")
        message=startingword+trying2
        print(message)
decrepeted()

