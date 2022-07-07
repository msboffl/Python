T = int(input("enter t"))
for _ in range(T):
    x = int(input("enter x"))
    y = float(input("enter y"))
    if( x % 5 == 0):
        print(y-(x + 0.5))
    elif(x > y):
        print(y)
    else:
        print(y)