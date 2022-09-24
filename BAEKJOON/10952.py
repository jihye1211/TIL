while(True):
    A,B = map(int,input().split())
    if(0<A and B<10):
        print(A+B)
    elif(A == 0 and B == 0):
        break
    else:
        False