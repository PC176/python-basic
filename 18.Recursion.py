#calling a function by itself is called recursion
i=0
def greet():
    global i
    i+=1
    print("Good Morning!",i)
    greet()
greet()
print("-------------------------")
# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
# i=0
# def greet():
#     global i
#     i+=1
#     print("Good Morning!",i)
#     greet()

