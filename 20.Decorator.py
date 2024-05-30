# we can add new feature in existing fuction withought disturbing that function is called decorater
a = int(input("Enter a no.:"))
b = int(input("Enter a no.:"))


def sub(a, b):
    c = a-b
    return c


def smart_sub(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


sub1 = smart_sub(sub)
print(sub1(a, b))
