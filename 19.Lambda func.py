#it is a anonymous function withought name
f = lambda a:a*a
result =f(5)
print(result)
s = lambda a,b : a+b
result = s(6,5)
print(result)
print("----------------------------")
#Use of lambda function
#1st in filter(func.,litrals)
# def eve(n):
#     return n%2==0
lst = [12,3,2,34,54,44,4,8,9]
# evens = list(filter(eve,lst))
evens = list(filter(lambda n:n%2==0,lst))
print(evens)
#we can use lambda in place of function eve
#2nd we can use in map and reduce function
doubles = list(map(lambda n:n*2,evens))
print(doubles)
from functools import reduce
sum = reduce(lambda a,b:a+b,doubles)
print(sum)