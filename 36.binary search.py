#to run binary search objects should be always in sorted form
#Biary search
pos=-1
list = [2, 4, 5, 6, 10, 34, 56, 68]
n = int(input("Enter a no. to search-"))
def search(list, n):
    global pos
    F = 0
    L = len(list)-1
    while F<=L:
        M = (L + F) // 2
        if list[M]==n:
            globals()['pos']=M
            return True
        else:
            if list[M]<n :
                F = M+1
            else:
                L = M-1
    return False
if (search(list, n)):
    print("Found at",pos+1)
else:
    print("Not Found")