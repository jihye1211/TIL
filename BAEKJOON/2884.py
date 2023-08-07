H,M = input().split(' ')

H = int(H)
M = int(M)-45

if(M<0):
    M = 60+M
    if(H==0):
        H = 23
    else:
        H -= 1
print(H,M)