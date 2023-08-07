x = int(input())
n = int(input())
m = 0

for i in range(n):
    a, b = map(int, input().split())
    m += a*b

if x == m:
    print("Yes")
else:
    print("No")
