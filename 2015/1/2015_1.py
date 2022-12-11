f = open("1\input.txt", "r")
data = f.read()

# Part 1
up = data.count("(")
down = data.count(")")
end = up - down
print("Part 1: " + str(end))

# Part 2
end = 0
up = 0
down = 0
char = 0
while (end >= 0):
	char = char + 1
	f = open("1\input.txt", "r")
	data = f.read(int(char))
	up = data.count("(")
	down = data.count(")")
	end = up - down
	#print(data)
	up = 0
	down = 0
print("Part 2: " + str(char))
