N = int(input())
direction = list(map(int, input().split()))
cnt1 = 0
cnt2 = 0
num = direction[0]

for i in range(len(direction)):
    if (direction[i] == num) :
        if(direction[i]==1) :
            cnt1+=1
        else:
            cnt2+=1
    else:
        num = direction[i]
        continue
if(cnt1>cnt2):
    print(cnt1)
else:
    print(cnt2)