#selection sorting
def sort(list):
    for i in range(len(list)-1):
        minpos = i
        for j in range(i,len(list)):
            if list[j]<list[minpos]:
                minpos = j
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp
list =[3,445,23,323,44,23,442,22,323,23,355,66,56]
print(list)
sort(list)
print(list)