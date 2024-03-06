import re

regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
def check(email):
    if(re.fullmatch(regex,email)):
        print("valid Email...")
    else:
        print("Invalid Email...")
ch=1
while(ch==1):
    x=input("Enter the email: ")
    check(x)
    ch=int(input("Do you want to continue(1/0)"))


