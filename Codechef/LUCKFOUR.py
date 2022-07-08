T = int(input("Enter Test Cases: "))
for _ in range(T):
    num = int(input("Enter the Number: "))
    count = 0
    while(num != 0):
        rem  = num % 10
        if(rem == 4):
            count += 1
        num = num // 10
    print(count)
