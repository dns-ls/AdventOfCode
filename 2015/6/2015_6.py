file_path = "2015/6/input.txt"
lines = []
try:
    with open(file_path, "r") as file:
        lines = file.readlines()
        pass
except FileNotFoundError:
    print(f"File '{file_path}' not found.")


# PART 1

# create matrix
matrix=[] 
for i in range(1000):
    row=[]
    for j in range(1000):
        row.append(0)
    matrix.append(row)

# parsing functions
for i in range(len(lines)):
    lines[i] = lines[i].replace("turn ", "")
    lines[i] = lines[i].replace("through ", "")
    lines[i] = lines[i].replace(",", " ")
    lines[i] = lines[i].split(" ")
    lines[i][4] = lines[i][4].replace("\n", "")
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            lines[i][j] = int(lines[i][j])
        else:
            pass

# used functions
def turn_on(startx, starty, stopx, stopy):
    for x in range(startx, stopx+1):
        for y in range(starty, stopy+1):
            matrix[x][y] = 1

def turn_off(startx, starty, stopx, stopy):
    for x in range(startx, stopx+1):
        for y in range(starty, stopy+1):
            matrix[x][y] = 0

def toggle(startx, starty, stopx, stopy):
    for x in range(startx, stopx+1):
        for y in range(starty, stopy+1):
            if matrix[x][y] == 0:
                matrix[x][y] = 1
            else:
                matrix[x][y] = 0

# main part?
for i in range(len(lines)):
    if lines[i][0] == "on":
        turn_on(lines[i][1],lines[i][2],lines[i][3],lines[i][4])
    elif lines[i][0] == "off":
        turn_off(lines[i][1],lines[i][2],lines[i][3],lines[i][4])
    else:
        toggle(lines[i][1],lines[i][2],lines[i][3],lines[i][4])

sol1 = 0

for i in range(len(matrix)):
    sol1 = sol1 + matrix[i].count(1)

# PART 2

matrix=[] 
for i in range(1000):
    row=[]
    for j in range(1000):
        row.append(0)
    matrix.append(row)

def p2_on(startx, starty, stopx, stopy):
    for x in range(startx, stopx + 1):
        for y in range(starty, stopy + 1):
            matrix[x][y] = matrix[x][y] + 1

def p2_off(startx, starty, stopx, stopy):
    for x in range(startx, stopx + 1):
        for y in range(starty, stopy + 1):
            if matrix[x][y] > 0:
                matrix[x][y] = matrix[x][y] - 1
            else:
                pass

def p2_toggle(startx, starty, stopx, stopy):
    for x in range(startx, stopx + 1):
        for y in range(starty, stopy + 1):
            matrix[x][y] = matrix[x][y] + 2

sol2 = 0

for i in range(len(lines)):
    if lines[i][0] == "on":
        p2_on(lines[i][1],lines[i][2],lines[i][3],lines[i][4])
    elif lines[i][0] == "off":
        p2_off(lines[i][1],lines[i][2],lines[i][3],lines[i][4])
    else:
        p2_toggle(lines[i][1],lines[i][2],lines[i][3],lines[i][4])

for i in range(len(matrix)):
    sol2 = sol2 + sum(matrix[i])

print("Part 1:", sol1)
print("Part 2:", sol2)