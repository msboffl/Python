T = int(input("Enter Test Cases: "))
for _ in range(T):
    A, B, C = map(int, input().split(" "))
    if(A + B + C == 180):
        print("YES")
    else:
        print("NO")