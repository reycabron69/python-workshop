n=int(input("how series should be : "))
a=0
b=1
L=[a]
for i in range(n-1):
             L.append(b)
             i=a+b
             a=b
             b=i
             
print(*L)
