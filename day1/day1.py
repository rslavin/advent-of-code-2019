with open("day1.in", 'r') as infile:
    print(sum(map(lambda a: int(int(a) / 3) - 2, infile.readlines())))
