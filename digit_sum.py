#Calculating sum of the digits present in the string
s=input("Enter a string:")
sum=0
for a in s:
    if a.isdigit():
        sum+=int(a)
print("Sum of String's digit is", sum)
