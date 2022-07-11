T = int(input("Enter the Test Cases: "))
for _ in range(T):
    X, Y = map(int, input().split(" "))
    print(abs(X-Y))