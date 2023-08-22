dane = [
    [23, 4, True, False],
    [18, 3, True, False],
    [8, 2, True, False],
    [200, 30, True, False],
    [8, 150, False, False],
    [30, 350, False, False],
    [5, 100, False, False],
    [10, 200, False, False],
    [36, 10, True, False]
]

# True = Obraczka | a > 0
# False = Dlugopis | a < 0

w1 = -2
w2 = 0.1

b = 6
const_d = 0.2


def neuron(x1, w1, x2, w2, b, const_d):
    a = ((x1 * w1) + (x2 * w2)) + b
    return a


i = 0
for j in range(1, 100):
    print(j, ">>>>>>>>>>>>>")
    for stage in dane:

        i += 1
        if j > 1:
            if stage[3] == True:
                w1 = w1 + (stage[0] * const_d * 1)
                w2 = w2 + (stage[1] * const_d * 1)
                b = b + 1 * const_d
            elif stage[3] == False:
                w1 = w1 + (stage[0] * const_d * -1)
                w2 = w2 + (stage[1] * const_d * -1)
                b = b + -1 * const_d


            if stage[2] != stage[3]:
                print(f'{i} >>> x1: {stage[0]}, x2: {stage[1]}', end="")
                a = neuron(stage[0], w1, stage[1], w2, b, const_d)

                if a > 0:
                    stage[3] = True
                elif a < 0:
                    stage[3] = False

                print(f' | a >>> {a}')
            else:
                print(f'--- {i} >>> x1: {stage[0]}, x2: {stage[1]}', end="")
                a = neuron(stage[0], w1, stage[1], w2, b, const_d)

                if a > 0:
                    stage[3] = True
                elif a < 0:
                    stage[3] = False

                print(f' | a >>> {a}')
        else:
            print(f'{i} >>> x1: {stage[0]}, x2: {stage[1]}', end="")
            a = neuron(stage[0], w1, stage[1], w2, b, const_d)

            if a > 0:
                stage[3] = True
            elif a < 0:
                stage[3] = False

            print(f' | a >>> {a}')
