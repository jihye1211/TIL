n = int(input())

for _ in range(n):
    sum = 0
    cnt = 0
    listtc = list(input())

    for k in listtc :
        if(k=="O") :
            cnt += 1
            sum += cnt
        elif(k=="X") :
            cnt = 0
    print(sum)