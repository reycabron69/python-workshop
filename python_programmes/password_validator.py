s=input()

num={chr(i) for i in range(47,58)}
low={chr(i) for i in range(65,91)}
upp={chr(i) for i in range(97,123)}

n=0
sp=0

if len(s)<7:
    print('Weak')
else:
    for i in s:
        if i in num:
            n+=1
        elif i not in low|upp:
            sp+=1
    else:
        if n>=2 and sp>=2:
            print('Strong')
        else:
            print('Weak')
