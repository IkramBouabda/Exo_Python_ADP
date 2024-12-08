nbr1=int(input("give me a number : "))
nbr2=int(input("give me another number : "))
choice=input("choose one of these 3 operators : + , * or -")
if choice=="+":
    choice1=nbr1+nbr2
    print(f"{nbr1}+{nbr2}={choice1}")
elif choice=="*":
    choice2=nbr1*nbr2
    print(f"{nbr1}*{nbr2}={choice2}")
elif choice=="-":
    choice3=nbr1-nbr2
    print(f"{nbr1}-{nbr2}={choice3}")
else:
    print("chooooose one")