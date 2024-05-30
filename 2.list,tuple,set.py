#list and tuple
#List
list = [8,'iii',99.99,'987',9+9j,"ioiuuy"] #different type of data we can store
#   add. =[0,1,2,3,4,5]    mutable
print(list)
print(list[0])
print(list[0:4])
print(list[3:6])
list[3]="prttt"
print(list)
print("------------------------")
#Tuple
tuple=(0,3,"trswf",88.8876,9+8j)
print(tuple)
#tuple[3] = "rrr" immutable
#some inbuilt in function
print("------------------------")
list = [2,45,12,87,55.55,77]
print(min(list))
print(max(list))
list.sort()
print(list)
list.extend([3,2,3])
print(list)
del list[4:]
print(list)
list.pop()
print(list)
list.pop(2)
print(list)
list.insert(2,34)
print(list)
print(tuple.count)

#List is mutable and Tuple is immutable
#Tuple is more secure for privet data and faster than list
print("-------------------------")
#Set
#no duplicatess
s = {22,25,4,656,875,55}
print(s)
print(type(s))
print(type(list))
print(type(tuple))
print("-----------")
#reverse a list
list1=[34,34,5,4,5,4,3,34,5,6,6,7,8,0]
list1.reverse()
print(list1)
list2=[]
for i in range(len(list1)-1,-1,-1):
    list2.append(list1[i])
print(list2)
    
    
