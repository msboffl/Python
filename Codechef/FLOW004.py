T = int(input("Enter Test Cases: "))
for _ in range(T):
    num = list(input("Enter Number: "))
    add = int(num[0]) + int(num[len(num)-1])
    print(add)
