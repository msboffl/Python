T = int(input("Enter Test Cases: "))
for _ in range(T):
    x = int(input("Enter the X value: "))

    if(x >= 1 and x < 100):
        print("Easy")
    elif(x >= 100 and x < 200):
        print("Medium")
    else:
        print("Hard")