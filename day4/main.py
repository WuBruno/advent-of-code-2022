from collections import Counter

def main():
    pairs = open("input.txt", "r")

    total = 0

    for pair in pairs:
        fst, snd = pair.split(',')
        fst_l, fst_r = fst.split('-')
        snd_l, snd_r = snd.split('-') 
        fst_l, fst_r, snd_l, snd_r = int(fst_l), int(fst_r), int(snd_l), int(snd_r)

        if fst_l <= snd_l and fst_r >= snd_r:
            total += 1
        elif fst_l >= snd_l and fst_r <= snd_r:
            total += 1

    return total

def main2():
    pairs = open("input.txt", "r")

    total = 0

    for pair in pairs:
        fst, snd = pair.split(',')
        fst_l, fst_r = fst.split('-')
        snd_l, snd_r = snd.split('-') 
        fst_l, fst_r, snd_l, snd_r = int(fst_l), int(fst_r), int(snd_l), int(snd_r)

        if fst_l <= snd_r or snd_l <= fst_r:
            total += 1

    return total

print(main())
print(main2())
