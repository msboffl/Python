T = int(input("Enter Test Cases"))
for _ in range(T):
    A, B, X = map(int, input().split(" "))
    print((B-A)//X)
