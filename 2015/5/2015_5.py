file_path = "2015/5/input.txt"
lines = []
try:
    with open(file_path, "r") as file:
        lines = file.readlines()
        pass
except FileNotFoundError:
    print(f"File '{file_path}' not found.")

# PART 1
nice_counter = 0

def three_vowels(string):
    if sum(1 for char in string if char in 'aeiou') > 2:
        return True
    else:
        return False

def no_naughty(string):
    if "ab" in string or "cd" in string or "pq" in string or "xy" in string:
        return False
    else:
        return True
    
def double_letter(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
        else:
            pass
    return False

for string in lines:
    if double_letter(string) and no_naughty(string) and three_vowels(string):
        nice_counter = nice_counter + 1
    else:
        pass

# PART 2
nice2 = 0

def appears_twice(string):
    for i in range(len(string)-4):
        searchfor = string[i:i+2]
        j = string[i+2::]
        if searchfor in j:
            return True
        else:
            pass
    return False
    

def repeats_letter(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    else:
        return False

for string in lines:
    if appears_twice(string) and repeats_letter(string):
        nice2 = nice2 + 1
    else:
        pass


print("Part 1:", nice_counter)
print("Part 2:", nice2)