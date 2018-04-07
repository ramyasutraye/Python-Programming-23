a=int(input("Enter number:"))
no=a
rev=0
while(a>0):
    dig=a%10
    rev=rev*10+dig
    a=a//10
if(no==rev):
    print("palindrome")
else:
    print("not palindrome")
