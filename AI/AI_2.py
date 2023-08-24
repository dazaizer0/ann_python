# zamien is positive na czy jest poprawne i jakie powu=inno byc a nie jakie jest
file = open("aidata.js", 'a')

class Neuron:
    def __init__(self, x, w, answer: bool, nreturn: bool):
        self.x = x
        self.w = w
        self.answer = answer
        self.nreturn = nreturn


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

def LOG(x, w, b, a, nret, answ):
    file.write(f'FIRST >> W: {w}\n')
    file.write(f'BEFORE >> W: {w}, B: {b}, IS_POSITIVE: {answ}\n')
    file.write(f'AFTER >> W: {w}, B: {b}, IS_POSITIVE: {answ}\n')
    file.write(f'>> {a}\n')
    file.write('\n')


D = 0.01
B = 4
A = 0

neuron1 = Neuron([18, 34], [2, 3], False, not False)

i = 1
while neuron1.nreturn != neuron1.answer:
    if i == 1:
        A = ACTIVATE(neuron1, B)

        print(f'FIRST >> W: {neuron1.w}, B: {B}')
        print(f'{i} >> {A}')

        if neuron1.answer == True:
            if A > 0:
                neuron1.nreturn = True
            elif A < 0:
                neuron1.nreturn = False
        else:
            if A < 0:
                neuron1.nreturn = False
            elif A < 0:
                neuron1.nreturn = True

        if neuron1.answer == neuron1.nreturn:
            if neuron1.answer == True:
                print("Obraczka")
                file.write('obraczka\n')
            else:
                print("Dlugopis")
                file.write('dlugopis\n')
        else:
            print("...")

        LOG(neuron1.x, neuron1.w, B, A, neuron1.nreturn, neuron1.answer)
        print()
    else:
        is_positive = neuron1.answer

        print(f'BEFORE >> W: {neuron1.w}, B: {B}, IS_POSITIVE: {is_positive}')

        neuron1.w = RETURN_NEW_W(D, neuron1.w, neuron1.x, is_positive)
        B = RETURN_NEW_B(D, B, is_positive)

        print(f'AFTER >> W: {neuron1.w}, B: {B}, IS_POSITIVE: {is_positive}')
        A = ACTIVATE(neuron1, B)
        print(f'{i} >> {A}')

        if neuron1.answer == True:
            if A > 0:
                neuron1.nreturn = True
            elif A < 0:
                neuron1.nreturn = False
        else:
            if A < 0:
                neuron1.nreturn = False
            elif A < 0:
                neuron1.nreturn = True

        if neuron1.answer == neuron1.nreturn:
            if neuron1.answer == True:
                print("Obraczka")
                file.write('obraczka\n')
            else:
                print("Dlugopis")
                file.write('dlugopis\n')
        else:
            print("...")

        LOG(neuron1.x, neuron1.w, B, A, neuron1.nreturn, neuron1.answer)
        print()
    i += 1


file.write(f'{A} | {neuron1.w} | {B} | {neuron1.answer}\n')
file.close()
