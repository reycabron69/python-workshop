a=int(input('Enter 1st no.: '))
b=int(input('Enter 2nd no.:'))

op=input('Enter the operator : ')

while op in ['+','-','*','/','//','%','^']:
             if op=='+':
                          a=a+b
                          print('the SUM is :',a)
             elif op=='-':
                          a=a-b
                          print('the Difference is :',a)
             elif op=='*':
                          a=a*b
                          print('the PRODUCT is : ',a)
             elif op=='/':
                          a=a/b
                          print('the Quotient is :',a)
             elif op=='//':
                          a=a//b
                          print('the integral Quotient is :',a)
             elif op=='%':
                          a=a%b
                          print('the REMAINDER is',a)
             elif op=='^':
                          a=a**b
                          print('the result is : ',a)
             op=input('Enter the operator : ')
             b=int(input('Enter 2nd operand :'))
else:
             print('Invalid operator')
