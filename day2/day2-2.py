input_o = [int(a) for a in open("day2.in").read().split(",")]
for n in range(100):
    for v in range(100):
        input = input_o[:]
        input[1:3] = [n, v]
        for idx in range(0, len(input), 4):
            if input[idx] == 99:
                break
            op, arg1, arg2, res = input[idx:idx + 4]

            if input[idx] == 1:
                input[res] = input[arg1] + input[arg2]
            elif input[idx] == 2:
                input[res] = input[arg1] * input[arg2]

        if input[0] == 19690720:
            print(str(100 * n + v))
            exit()
