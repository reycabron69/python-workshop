y=int(input("Enter a Year : "))

if y%4==0:
             if y%100==0:
                          if y%400==0:
                                       print("LEAP")
                          else:
                                       print("Not Leap")
             else:
                          print("Leap")
else:
             print("Not Leap")
             
