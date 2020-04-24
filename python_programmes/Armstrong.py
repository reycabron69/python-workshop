n=int(input("Enter a no. : "))
t=n
s=0
while t:
             r=t%10
             q=t//10
             t=q
             s+=(r**3)

if s==n:
             print('Armstrong',s)
else:
             print('Not Armstrong',s)
