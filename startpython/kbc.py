def sasta():
    price=0
    x=int(input("enter the 2+2\n"))
    if(x==4):
        price += 1
        x=str(input("what is your name \n"))
        if(x=="naveen" or x=="Naveen"):
            price+= 1
            x=str(input("what is your pet name \n"))
            if(x=='tom' or "Tom"):
                price+= 1
    print("your winning price is :-",price)





def mahanga():
    questions = [
        ["1 which language you are working at:", "python", "c++", "c", "none"],
        ["2 which language you are working at:", "python", "c++", "c", "none"],
        ["3 which language you are working at:", "python", "c++", "c", "none"],
        ["4 which language you are working at:", "python", "c++", "c", "none"],
        ["5 which language you are working at:", "python", "c++", "c", "none"],
        ["6 which language you are working at:", "python", "c++", "c", "none"],
        ["7 which language you are working at:", "python", "c++", "c", "none"],
        ["8 which language you are working at:", "python", "c++", "c", "none"],
        ["9 which language you are working at:", "python", "c++", "c", "none"],
    ]
    levels = ["1000", "2000", "3000", "4000", "5000", "50000","55000","75000","90000","0"]
    money = 0

    for i in range(0, len(questions)):
        question = questions[i]
        answer = int(input(f"the queston on your screen is:-\n {question[0]}\n a.{question[1]}\   b.{question[2]} \nc.{question[3]}   d.{question[4]} \n PRESS 0 TO QUIT  "))
        if answer == 0:
            money = levels[i - 1]
            break
        if( answer== 1):
            print (f"you won {levels[i]}\n\n")
            money = levels[i]
            if levels[i] == '3000':
                money = 3000
            elif levels[i] == '50000':
                money = 5000
        else:
            print("wrong answer")
            break

    print(f"\nthe amount you're taking home is {money}")







choose=int(input("choose which programe you want to run:- \n 1 for mahanga  \n 2 for sasta\n"))
if(choose==1):
    mahanga()
elif(choose==2):
    sasta()
else:
    print("wrong input")



    
