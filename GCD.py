n1=int(input("NUmbeer:"))
n2=int(input("NUmbeer:"))
for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        print(i)