s=input("Enter 1st:")
s1=input("Enter 2nd: ")

s=s.lower()
s1=s1.lower()


if sorted(s)==sorted(s1):
    print("True")

else:
    print("False")