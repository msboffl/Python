T = int(input("Enter Test Cases:"))
for _ in range(T):
    A, B = map(int, input().split(" "))
    if(A > B):
        print(">")
    elif(A < B):
        print("<")
    else:
        print("=")
