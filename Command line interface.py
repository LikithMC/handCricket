import tkinter as tk
import random
def bat():
    gtrunp=0
    k=0
    for i in plyrs:
        j=0
        trun=0
        print("Batsman : ",i)
        print("Bowler : ",compplyrs[k])
        print()
        while j<6:
            print("Computer has throw a ball")
            check1=True
            while check1:
                r=input("Enter your batting hit : ")
                if len(r)!=0 and r.isdigit() and 0<int(r)<7 :
                    break
                else:
                    print("                 =========================================")
                    print("                 The entered value is not within range 1-6")
                    print("                         Abide by the rules please")
                    print("                 =========================================")
                    print() 
            b=random.randrange(1,7)
            print()
            print("Ball thrown ",b,"Computer hit ",r)
            print()
            if int(r)==b:
                print("****Out*****")
                break
            trun+=int(r)
            j+=1
        print("*** Player ",i," turn completed ****")
        print(i," scored ",trun," runs")
        print()
        gtrunp+=trun
        k+=1
    return (gtrunp)
def bowl():
    gtrunc=0
    k=0
    for i in compplyrs:
        j=0
        trun=0
        print("Batsman : ",i)
        print("Bowler : ",plyrs[k])
        print()
        while j<6:
            print("Bats man is ready ")
            print()
            check1=True
            while check1:
                b=input("Throw a ball : ")
                if len(b)!=0 and b.isdigit() and 0<int(b)<7:
                    break
                else:
                    print("                 =========================================")
                    print("                 The entered value is not within range 1-6")
                    print("                         Abide by the rules please")
                    print("                 =========================================")
                    print()
            r=random.randrange(1,7)
            print("Ball thrown ",b,"Computer hit ",r)
            print()
            if r==int(b):
                print("****OUT*****")
                break
            trun+=r
            j+=1
        print("*** Player ",i," turn completed ***")
        print
        print(i," scored ",trun," runs")
        print()
        gtrunc+=trun
        k+=1
    return (gtrunc)
print("HI PlEASE REGISTER YOURSELF")
coach=input("Start by entering the name of the team Coach :")
print()
print("Hi",coach,"welcome to hand cricket league")
print("Remember dont take anything seriously, we play this cricket with just 3 players")
print("Also due to time management we allow each player to play for a max of one over")
print("(If he doesnt become out by then)")
print()
print("**********")
print("Please play using numbers only between 1 to 6")
print("**********")
print()
print()
compplyrs=["Bommai","HD Kswamy","Siddu"]
plyrs=list()
i=0
j=1
while i<=2:
    print("Enter name of player no",j," :")
    a=input("")
    plyrs.append(a)
    i+=1
    j+=1
print()
print("Your team members are",plyrs)
print()
check=True
while check:
    tos=input("Enter Head or Tail for the purpose of toss ").casefold()
    if isinstance(tos,str)and(tos.casefold()=="head" or tos.casefold()=="tail"):
        check=False
    else:
        print("The entered value of toss is not matching")
        print("Please check your spelling and re_enter")
        print()
etos=random.choice(["Head","Tail"]).casefold()
if tos==etos:
    print("You won the toss")
    print()
    check=True
    while check:
        choice=input("Bat or Bowl ? ").casefold()
        if isinstance(choice,str):
            if choice=="bat":
                print("-----------------------YOU CHOSE TO BAT ------------------------")
                print()
                totalrunsplayer= bat()
                print()
                print("----------------------------------------------------------------")
                print("                       BATTING TERM COMPLETED")
                print("                       ITS YOUR TIME TO BOWL")
                print("-----------------------------------------------------------------")
                print()
                totalrunscomp= bowl()
                check=False
            elif choice=="bowl":
                print("----------------------YOU CHOSE TO BOWL--------------------------")
                print()
                totalrunscomp= bowl()
                print()
                print("-----------------------------------------------------------------")
                print("                       BOWLING TERM COMPLETED")
                print("                       ITS YOUR TIME TO BAT")
                print("-----------------------------------------------------------------")
                print()
                totalrunsplayer= bat()
                check=False
            elif choice!="bat" and choice!="bowl" and len(choice)!=0:
                print("The spelling may not be correct please RE-ENTER")
                print()
            else:
                print("Please Type your choice and then press enter")
                print()
else:
    print("You lost the toss")
    print()
    print("-------------------------YOU HAVE TO BOWL------------------------ ")
    print()
    totalrunscomp = bowl()
    print()
    print("-----------------------------------------------------------------")
    print("                       BOWLING TERM COMPLETED")
    print("                       ITS YOUR TIME TO BAT")
    print("-----------------------------------------------------------------")
    print()
    totalrunsplayer = bat()
print("The runs scored by team ",coach," is ",totalrunsplayer)
print("The runs scored by team computer is ",totalrunscomp)
print()
if totalrunscomp > totalrunsplayer:
    print("Computer won by",(totalrunscomp-totalrunsplayer)," runs")
if totalrunsplayer > totalrunscomp:
    print("You won by",(totalrunsplayer-totalrunscomp)," runs")
    print()
print("Thank you")

screen=tk.Tk()
screen.geometry('900x300')
screen.title("HAND CRICKET")
if totalrunscomp > totalrunsplayer:
    m="Computer won by "+str(totalrunscomp-totalrunsplayer)+" runs"
if totalrunsplayer > totalrunscomp:
    m="You won by "+str(totalrunsplayer-totalrunscomp)+" runs"
m2="Thank You"
Label=tk.Label(text=m,fg="lime",bg="black",width="100",height='10')
Label2=tk.Label(text=m2,fg="black",bg="lime",width="100",height='10')
Label.pack()
Label2.pack()
screen.mainloop()