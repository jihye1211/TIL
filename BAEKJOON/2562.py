i = 0
N = []
while i< 9:
    s = int(input())
    N.append(s)
    i+=1
    
print(max(N))
print(N.index(max(N))+1)