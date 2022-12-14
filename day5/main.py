from collections import deque 

def main():
    text_input = open("input.txt", "r")
    stacks = [deque() for i in range(9)]

    for n, line in enumerate(text_input):
        if n < 9:
            for i, c in enumerate(line):
                if c.isupper():
                    stacks[(i + 2)//4].append(c)

        elif n >= 10:
            _, x, _, a, _, b = line.split(" ");

            for _ in range(int(x)):
                v = stacks[int(a)-1].pop()
                stacks[int(b)-1].append(v)
    
    return "".join([x.pop() for x in stacks])

print(main())
