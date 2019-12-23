input = [int(a) for a in open("day2.in").read().split(",")]
input[1:3] = [12, 2]
for idx in range(0, len(input), 4):
    op, arg1, arg2, res = input[idx:idx + 4]

    if op == 1:
        input[res] = input[arg1] + input[arg2]
    elif op == 2:
        input[res] = input[arg1] * input[arg2]
    elif op == 99:
        break

print(input[0])