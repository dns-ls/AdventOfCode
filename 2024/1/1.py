with open("./input.txt", "r") as file:
    input = file.read()

lines = input.strip().split('\n')
x = []
y = []

for line in lines:
    values = line.split()
    x.append(int(values[0]))
    y.append(int(values[1]))
x.sort()
y.sort()

sum1 = 0
for i in range(len(x)):
    a = x[i] - y[i]
    if a < 0:
        a = a * -1
    sum1 +=a
print(sum1)

sum2 = 0
for i in range(len(x)):
    sum2 += x[i] * y.count(x[i])


print("Part 1: ", sum1, "Part 2: ", sum2)