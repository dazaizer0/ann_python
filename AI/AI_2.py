# zamien is positive na czy jest poprawne i jakie powu=inno byc a nie jakie jest
class Neuron:
    def __init__(self, x, w, answer: bool):
        self.x = x
        self.w = w
        self.answer = answer


def ACTIVATE(n: Neuron,
             b: float) -> float:
    for i in range(0, len(n.x), 2):
        a = ((n.x[i] * n.w[i]) + (n.x[i + 1] * n.w[i + 1])) + b
        return a


def RETURN_NEW_W(d, w, x, is_positive):
    if is_positive:
        for i in range(0, len(w)):
            w[i] = w[i] + x[i] * d * 1
    else:
        for i in range(0, len(w)):
            w[i] = w[i] + x[i] * d * -1

    return w


def RETURN_NEW_B(d, b, is_positive):
    if is_positive:
        return b + 1 * d
    else:
        return b + -1 * d


def TEACH(n: Neuron):
    print(n.x)
    print(n.w)


D = 0.2
B = 6
A = 0

neuron1 = Neuron([23, 4], [-2, 0.1], True)
for i in range(1, 50):
    if i == 1:
        A = ACTIVATE(neuron1, B)

        print(f'FIRST >> W: {neuron1.w}, B: {B}')
        print(f'{i} >> {A}')

        if A > 0:
            print("O+")
        else:
            print("D-")

        print()
    else:
        is_positive = neuron1.answer

        # ACTIONS
        print(f'BEFORE >> W: {neuron1.w}, B: {B}, IS_POSITIVE: {is_positive}')

        neuron1.w = RETURN_NEW_W(D, neuron1.w, neuron1.x, is_positive)
        B = RETURN_NEW_B(D, B, is_positive)

        print(f'AFTER >> W: {neuron1.w}, B: {B}, IS_POSITIVE: {is_positive}')
        A = ACTIVATE(neuron1, B)
        print(f'{i} >> {A}')

        if A > 0:
            print("O+")
        else:
            print("D-")

        print()
