def factorial(n):
             if n==1:
                          return 1
             return n*factorial(n-1)

while (True):
             num=int(input('Enter a positive no: '))
             print('Factorial of ',num,' is : ',factorial(num))
                          
