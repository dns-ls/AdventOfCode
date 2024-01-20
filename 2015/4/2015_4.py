import hashlib

input = "bgvyzdsv"

# PART 1
counter1 = 0
ans1 = int()

while str(ans1)[0:5] != "00000":
    ans1 = hashlib.md5((input + str(counter1)).encode()).hexdigest()
    counter1 = counter1 + 1

# PART 2
counter2 = 0
ans2 = int()

while str(ans2)[0:6] != "000000":
    ans2 = hashlib.md5((input + str(counter2)).encode()).hexdigest()
    counter2 = counter2 + 1

print("Part 1:", counter1)
print("Part 2:", counter2)
