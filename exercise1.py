name = input("Hey body , please enter your name : ")
if name=="VIP":
    print("Enjoy the show for free !")
else :
    number_tickets=int(input("How lany tickets would you like to buy ? : "))
    total_cost=number_tickets*15.50
    print(f"The total cost is : {total_cost} $")
    print("Enjoy your tickets !")