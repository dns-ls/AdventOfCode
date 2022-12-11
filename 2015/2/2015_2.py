import statistics

f = open("2\input.txt", "r")
data = f.read()

total = 0 #total surface
lnum = 0 #line number
total_ribbon = 0

for line in data:
    current = data.splitlines()[lnum]
    slength, swidth, sheight = current.split("x") #this converts to strings not ints
    length = int(slength)
    width = int(swidth)
    height = int(sheight)
    lw = length * width
    wh = width * height
    hl = height * length
    smallestside = min(lw, wh, hl)
    surface = 2*(lw+wh+hl) + smallestside
    total = total + surface
    lnum = lnum + 1

    small_size =  min(length, width, height)
    medium_size = statistics.median([length, width, height])
    ribbon =  2*small_size + 2*medium_size + length*width*height
    total_ribbon = total_ribbon + ribbon
    print("Total Wrapping Paper: ", total, "\n", "Total Ribbon: ", total_ribbon)
    # Eventually, lnum becomes greater than the amount of total lines and it crashes,
    # but the last number is the answer :)
print(total)
