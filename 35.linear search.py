#lineat search
pos=-1
list = [2, 4, 5, 4, 6, 65, 54, 33, 32]
n = int(input("Enter a no. to search-"))
def search(list, n):
    i=0
    global pos
    while i <= (len(list)-1):
      if  list[i] == n:
          pos = i
          return True
      else:
          i=i+1
    return False
if (search(list, n)):
    print("Found at",pos+1)
else:
    print("Not Found")