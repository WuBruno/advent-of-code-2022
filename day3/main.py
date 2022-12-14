import string

def main():
    input = open("input.txt", "r")

    group = set()
    i = 0
    total = 0

    for line in input:
        curr = set(line.strip())

        if i % 3 == 0:

            if i > 0:
                total += extract_value(group)

            group = curr
        else:
            group = group.intersection(curr)

        i += 1

    total += extract_value(group)

    return total

def extract_value(group):
    values = {x: i+1 for i, x in enumerate(string.ascii_lowercase + string.ascii_uppercase)}
    (letter, ) = group

    return values[letter]

print(main())
