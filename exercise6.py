price = float(input("Enter the price in dinars : "))

dinars = int(price)  # int part
centimes = round((price - dinars) *100)  #decimal part 

print(f"The price is {dinars} dinars and {centimes} centimes.")