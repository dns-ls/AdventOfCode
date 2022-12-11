f = open("3\\input.txt", "r")
data = f.read()

# PART 1
posX = 0
posY = 0
visitedPos = [(0,0)]

while data:
    currentChar = data[0]
    match currentChar:
        case "<":
            posX -= 1
        case "^":
            posY += 1
        case ">":
            posX += 1
        case "v":
            posY -= 1
    visitedPos.append((posX, posY))
    data = data[1:]
mylist = list(dict.fromkeys(visitedPos))
print("Answer Part 1: ", len(mylist))

#PART 2
posX1 = 0
posY1 = 0
posX2 = 0
posY2 = 0
visitedPos = [(0,0)]
turn = 1
f = open("3\\input.txt", "r")
data = f.read()

while data:
    currentChar = data[0]
    if (turn % 2) == 0:
        match currentChar:
            case "<":
                posX1 -= 1
            case "^":
                posY1 += 1
            case ">":
                posX1 += 1
            case "v":
                posY1 -= 1
        visitedPos.append((posX1, posY1))
        data = data[1:]
        turn +=1
    else:
        match currentChar:
            case "<":
                posX2 -= 1
            case "^":
                posY2 += 1
            case ">":
                posX2 += 1
            case "v":
                posY2 -= 1
        visitedPos.append((posX2, posY2))
        data = data[1:]
        turn += 1
mylist = list(dict.fromkeys(visitedPos))
print("Answer Part 2: ", len(mylist))
