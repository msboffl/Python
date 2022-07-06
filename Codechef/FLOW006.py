T = int(input("Enter Test Cases: "))
for _ in range(T):
    n = int(input())
    sum = 0
    while(n != 0):
        rem = n % 10
        sum += rem
        n = n // 10
    print(sum)