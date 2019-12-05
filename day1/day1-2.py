def fuel(a):
    f = max(int(int(a) / 3) - 2, 0)
    return f + fuel(f) if f else f


with open("day1.in", 'r') as infile:
    print(sum(map(fuel, infile.readlines())))
