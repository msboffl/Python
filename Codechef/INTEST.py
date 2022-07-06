n, k = map(int, input("Enter Test Cases:").split())
count = 0
for _ in range(n):
    X = int(input())
    if(X % k == 0):
        count += 1
print(count)