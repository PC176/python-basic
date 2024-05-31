#errors - 1.compilation error 2.logical error 3.runtime error
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
try:
    print("Process start")
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    c=a/b
    print(c)
#except run only when error occurs
except ZeroDivisionError as e:
    print("We can not devide by zero -",e)
except ValueError as e:
    print("Value error",e)
except Exception as e:
    print("other error",e)
#finally run always
finally:
    print("Process end")

