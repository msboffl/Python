T = int(input("Enter Test Cases : "))
for _ in range(T):
    X, Y = map(int, input().split(" "))

    if(X == Y or X > Y):
        print("YES")
    else:
        print("NO")