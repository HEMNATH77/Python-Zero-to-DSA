Year = eval(input("Enter the Year:"))

if Year % 4 == 0 or Year % 100 == 0 and Year % 400 == 0:
    print("Leap Year")

else:
    print("Normal Year")