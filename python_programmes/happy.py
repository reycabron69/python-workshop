n=int(input("Enter a no. : "))

while n!=1:
             num=n
             n=0
             while num:
                          r=num%10
                          q=num//10
                          num=q
                          n+=(r**2)


print('happy' if n==1 else 'unhappy') 
                         
