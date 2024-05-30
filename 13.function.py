#functon d-e-f
def pro():   #definition
    print("Pratik pro")
pro()   #invoke function    
print("hello")
pro()
#we call these reusable pieces of code "function"
big = max("Hello pratik")
print(big)
tiny = min("HEllo pratik")
print(tiny)
#Argument parameter result(return)
def pro(p1):
     if p1==3:
        print("3")
     return 4
pro(3)    
print(pro(3))
def add(a,b):
    c=a+b
    #print(c)
    return c
x=add(3,4)
print(x)
def test():
    print("teddd")
test()
#random function 
import random
random.random()
print(random)
print("------------------------------")
#Main function
def get_integer():
    I = int(input("Enter a number:"))
    return I
def main():
    print(("started"))
    Output=get_integer()
    print(Output)
    
if __name__=="__main__":
    main()    
