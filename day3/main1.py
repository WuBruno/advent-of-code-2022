from collections import Counter
import string

def main():
    rucksacks = open("input.txt", "r")
    alphabet = string.ascii_lowercase +  string.ascii_uppercase

    total = 0
    values = { x: i+1 for i, x in enumerate(alphabet)}

    for rucksack in rucksacks:
        length = len(rucksack)
        first_comp = { x for x in rucksack[:length//2].strip() }
        second_comp = { x for x in rucksack[length//2:].strip() }

        error = first_comp.intersection(second_comp).pop()

        total += values[error]

    return total

def main2():
    rucksacks = open("input.txt", "r")

    alphabet = string.ascii_lowercase + string.ascii_uppercase
    values = { x: i+1 for i, x in enumerate(alphabet)}

    total = 0
    i = 0
    mem = {}
    appear = 0

    for rucksack in rucksacks:
        if i % 3 == 0:
            print()
            if mem:
                value = next(iter(mem))
                print(value, values[value])
                total += values[mem.pop()]

            mem = {x for x in rucksack.strip()}
            appear += 1
            print(i)
            
        i += 1
        curr = {x for x in rucksack.strip()}
        mem = mem.intersection(curr)
        print(mem, curr)
    
    return total, appear


print("Part 1: ", main())
print("Part 2: ", main2())
