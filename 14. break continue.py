# break and continue
while True:
    line = input("> ")
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print("done!")
print("-------------")
# dofor i in "RAMJIBLESSYOU":
for letter in 'geeksforgeeks':
    break
print('Last Letter :', letter)
