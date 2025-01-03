n = int(input("enter a number:"))
count = 0
while n != 0:
     n //= 10
     count +=1

print(""+str(count))

#By using inbuilt methods
#a = int(input("Enter a number:"))
#print(len(str(a)))