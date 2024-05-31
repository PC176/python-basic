#we can creat a gentators by using yield
#'yield' produces a value but retains the function's state, allowing it to resume from where it left off
def Squre():
    i=1
    while i<=10:
        sq = i*i
        yield sq
        i+=1


values = Squre()
for i in values:
    print(i)
