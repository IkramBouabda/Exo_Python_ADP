nbr = 10
i = 0
nbr1 = 0

while True :
    nbr1 = int(input("try to catch the number : "))
    i += 1
    if nbr1<nbr:
        print("Nah , the number is greater")
    elif nbr1>nbr:
        print("Nah , the number is samller")
    else :
        print("yeeeeah , you got the number")
