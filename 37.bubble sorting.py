#bubble sorting
def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j+1] < list[j]:
                temp = list[j]
                list[j]=list[j+1]
                list[j+1]=temp
list =[3,445,23,323,44,23,442,22,323,23,355,66,56]
print(list)
sort(list)
print(list)