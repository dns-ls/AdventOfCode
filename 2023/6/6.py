f = open("input.txt", "r")
data = f.read()
data = data.split()

a = list()
for i in range(1,5):
    a.append(list([int(data[i]), int(data[i+5])]))
print(a)

def func(time, distance):
    sum = 0
    for s in range(time):
        ht = time - s
        if ht * s > distance:
            sum += 1
            #print(sum)
    return sum

total = 1
sum = 0
for i in range(len(a)):
    sum = 0
    #sum = 0
    sum += func(a[i][0], a[i][1])
    #print(sum)
    total *= sum
print("Part 1: ",total)

### part 2
n_t = str()
n_d = str()
for i in range(len(a)):
    n_t = n_t + str(a[i][0])
    n_d = n_d + str(a[i][1])
n_t, n_d = int(n_t), int(n_d)

print("total part 2: ", func(n_t, n_d))