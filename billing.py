name=input("enter your name")
board=input("enter your board")
dest=input("enter your dest")
km=int(input("enter your km"))
date=input("enter your date")
facility=int(input("choose \n 1.normal \n 2.fast \n 3.super fast \n 4.express"))
price=1
if facility==1:
    price=km*1
    print("price is",price)
elif facility==2:
    price=km*5
    print("price is",price)
elif facility==3:
    price=km*10
    print("price is",price)
elif facility==4:
    price=km*15
    print("price is",price)
else:
    print("enter right choice")
print("name:",name)
print("board",board)
print("destination",dest)
print("kilometer",km)
print("date",date)
