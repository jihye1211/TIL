N = input()
if int(N) < 10:
    N = '0'+N
    num = 0
    sum = []
    sum.append(N)

    while True:
        a = str(int(sum[num][0])+int(sum[num][1]))
        if int(a) < 10:
            a = '0'+a
            sum.append(sum[num][1]+a[1])
            num += 1
        if sum[num] == N:
            break
        print(num)

