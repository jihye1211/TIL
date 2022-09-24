import sys
T = int(sys.stdin.readline())
for i in range(T):
    A,B = map(int,sys.stdin.readline().split())
    if (A>0 and A<1001) and (B>0 and B<1001)  :
        print(A+B)
    else :
        False