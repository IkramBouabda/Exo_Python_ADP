hourly_wage = 20.0
hours = 6
day = "sunday"

daily_wages = hourly_wage * hours
if day == "sunday":
    print("wagesbefore :", daily_wages)
    daily_wages *= 2
    print(f"Daily wages : {daily_wages} euros")