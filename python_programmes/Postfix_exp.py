T=int(input())
for i in range(0,T):
    stk=list()  #stack
    st=input()  #infix Expression

    s='('+st+')'  #adding parentheses
    P=""            #POSTFIX Expression

    pre={'+':1,'-':1,'*':2,'/':2,'%':2,'^':3}  #precedence dictionary

    for t in s:   #scanning expression
        #print(stk,P)
        if t=='(':
            stk.append(t)
        elif ord(t) in range(97,123) or ord(t) in range(65,91):
            P+=t
        elif t==')':
            tos=len(stk)-1
            while stk[tos]!='(':
                P+=stk[tos]
                del stk[tos]
                tos-=1
            del stk[tos]
        else:
            tos=len(stk)-1
            while stk[tos]!='(' :
                if pre[stk[tos]]<pre[t]:
                    break
                P+=stk[tos]
                del stk[tos]
                tos-=1

            stk.append(t)
    print(P)        #POSTFIX Expression OUTPUT
"""
stk=list()  #stack
st=input()  #infix Expression

s='('+st+')'  #adding parentheses
P=""

pre={'+':1,'-':1,'*':2,'/':2,'%':2,'^':3}

for t in s:   #scanning st
    print(stk,P)
    if t=='(':
        stk.append(t)
    elif ord(t) in range(97,123):
        P+=t
    elif t==')':
        tos=len(stk)-1
        while stk[tos]!='(':
            P+=stk[tos]
            del stk[tos]
            tos-=1
        del stk[tos]
    else:
        tos=len(stk)-1
        while stk[tos]!='(' :
            if pre[stk[tos]]<pre[t]:
                break
            P+=stk[tos]
            del stk[tos]
            tos-=1

        stk.append(t)

print(P)"""
            
            

    


        
