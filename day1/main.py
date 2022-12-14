def main():
    values = open("input.txt", "r")

    curr = 0
    totals = []

    for x in values:
        if x.strip().isnumeric():
            curr += int(x)
        else:
            totals.append(curr)
            curr = 0

    return sum(sorted(totals, reverse=True)[:3])

print(main())
