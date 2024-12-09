total_amount=float(input("Total amount : "))
number_items=int(input("Number of items : "))
day_of_week=input("Day of the week : ")
if day_of_week=="monday" or day_of_week=="tuesday" or day_of_week=="thursday" or day_of_week=="wednesday" or day_of_week=="thursday" or day_of_week=="friday" :
    total_amount=total_amount*0.1
    print(f"Total price after discount is : {total_amount}")
else :
    total_amount=total_amount*0.2
    print(f"Total price after discount is : {total_amount}")
