#program to capitalize every other letter in string
string=input("Enter a string: ")
length=len(string)
print("Original string is: ", string)
string2=' '
for a in range(0,length,2):
    string2+= string[a]
    if a < (length-1):
        string2+= string[a + 1].upper()
print("Alternatively capitalized string :", string2)
