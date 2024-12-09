import math

number_people=int(input("Hey ,how many people need a ride ? :"))
number_people_taxi = int(input("How many people can fit in one Taxi ? : "))
#math.ceil tkbr number vers le haut
number_of_taxis=math.ceil(number_people/number_people_taxi)
print(f"Number of taxis needed is : {number_of_taxis}")
