from collections import Counter

def main():
    text_input = open("input.txt", "r")
    msg = text_input.readline().strip()

    mem = Counter(msg[:4])

    for i, c in enumerate(msg[4:]):
        (_, most_common), = mem.most_common(1)

        if (most_common == 1):
           return i + 4
        
        mem[c] += 1
        mem[msg[i]] -= 1
    
    return "reached the end" + str(len(msg))

print(main())
