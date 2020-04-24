a,b,c=map(str,input("Enter 3 strings : ").split())
if len(a)>len(b) and len(a)>len(c):
             print(a)
elif len(b)>len(c):
             print(b)
else:
             print(c)
