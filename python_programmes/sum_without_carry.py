T=int(input())

for k in range(T):
    a,b=map(int,input().split())
    SUM=0
    mul=1
    
    while a or b:
        r1=a%10
        r2=b%10

        bit_sum=(r1+r2)%10

        SUM+=bit_sum*mul
        mul*=10
        
        a//=10
        b//=10

    print(SUM)
    
