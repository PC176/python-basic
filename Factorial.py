def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def rfact(n):
    print(__name__)
    if n==0:
        return 1
    return n*fact(n-1)

def main():
    n = int(input("Enter a number:"))
    result = fact(n)
    print(result)
    print("---------------------------------")
    n = int(input("Enter a number:"))
    result = rfact(n)
    print(result)

if (__name__)=="__main__":
    main()