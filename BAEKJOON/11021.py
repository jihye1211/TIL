import sys
T = int(sys.stdin.readline())
for i in range(T):
    A,B = map(int,sys.stdin.readline().split())
    if (A>0 and B<10)  :
        C = A+B
        print("Case #"+str(i+1)+":",A,"+",B,"=",C)
    else :
        False