
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
l="False"
while l=="False":
    r=""
    A=random.randint(0,12)
    C=random.randint(0,12)
    a=cards[A]
    print ("users card1:",a)
    B=random.randint(0,12)
    b=cards[B]
    print("computers first card",b)

    c=cards[C]
    k=0
    total=0
    print("users second card",c)
    if(a+c==21):
        r="blackjack"
    if(a+c>21):
        if(a==11):
            a=1
        elif(c==11):
            c=1
        else:
            print("user lost")
    b1=""
    D=0
    v=0
    d=0
    if(a+c<21):
        m=input("enter yes if u want another card, no if u dont want")
        if(m=="yes"):
            D=random.randint(0,12)
            d=cards[D]
            print("users third card",d)
            k=1
    if k==0:
        total=a+c
    elif k==1:
        total=a+c+d
    print(total)
    if(total>21):
        if d==11:
            d=1
            total=a+c+d
            if total>21:
                print("User lost")
                v=1

        else:
            print("User lost")
            v=1
    if total==21:
        b1="blackjack"
    if (v != 1):
        print("users total:",(total))
        p="True"

        n=0
        G=random.randint(0,12)
        g=cards[G]

        if(b+g==21):
            n=1
        if b+g<16:
            while (g+b<16):
                G=random.randint(0,12)
                g=cards[G]


        print("comp second card",g)
        tot=g+b
        if(tot>21):
            if(g==11):
                g=1
            elif(b==11):
                b=1
            else:
                print("user wins")
            tot=g+b
        if(n==1):
            print("computer blackjack wins")
        elif(tot==21):
            print("computer wins")
        elif(tot<total):
            print("user wins")
        elif(tot>total):
            print("computer wins")
        elif(tot==total):
            if(tot==21):
                print("computer wins")
            else:
                print("draw")
    j=input("enter yes if u wanna continue or no if u dont wanna")
    if(j=="yes"):
        l="False"
        print("\n"*20)
    else:
        l="True"
