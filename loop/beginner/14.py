#Count the digits in a number using a loop.
num=int(input("Enter the number: "))
rev=0
while num>0:
    digit = num%10
    rev=rev+1
    num=num//10
print (rev)