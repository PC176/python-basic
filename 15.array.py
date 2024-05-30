from  array import *
vals = array("i",[4,4,4,5,5,4])
print(vals)
for i in range(6):
    print(vals[i])
print(vals.buffer_info())
print(vals.typecode)
newarr= array(vals.typecode,(a*a for a in vals))
print(newarr)
#enter a no. by input
arr = array("i",[])
s = int(input("size of array"))
for i in range(s):
    val = int(input("enter a value of array"))
    arr.append(val)
print(arr)
val = int(input("enter a val to search"))
k=0
for e in arr:
    if val==e:
        print(k)
        break
    k+=1
print(arr.index(val))
del arr[1]
print(arr)