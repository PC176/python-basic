# while loop
i = 5
while i > 0:
    print("h", end="")
    j = 5
    while j > 0:
        print("i", end="")
        j = j-1
    i = i-1
    print()
# for loop
x = ["Hello", 45, 56.9]
for i in x:
    print(i)

for i in ["Hello", 45, 56.9]:
    print(i)

for i in range(1, 11):
    print(i)
for i in range(21, 2, -2):
    print(i)
# factorial
N = int(input("Enter a no."))
F = 1
for i in range(1, N+1):
    F = F*i
print("Factorial of {} is {}".format(N, F))
