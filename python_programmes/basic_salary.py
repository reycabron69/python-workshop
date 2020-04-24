basic=int(input("Enter Basic Salary : "))
sal=basic
if basic>=50000 and basic<60000:
         sal+=0.3*basic
elif basic>20000:
             sal+=.2*basic
elif basic>10000:
             sal+=.1*basic

print("Total Salary = ",sal)
