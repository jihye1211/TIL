N = input()
num = list(map(int,input().split()))
V = int(input())
cnt = 0
for i in range(len(num)):
    if(num[i] == V):
        cnt+=1

print(cnt)