runner1=input("First runner name is : ")
time1=float(input("Time (in seconds) is : "))
runner2=input("Second runner name is : ")
time2=float(input("Time (in seconds) is : "))
if time1>time2 :
    print(f"the faster runner is {runner1}")
elif time1<time2 :
    print(f"the faster runner is {runner2}")
else :
    print(f"{runner1} and {runner2} have the same time")
