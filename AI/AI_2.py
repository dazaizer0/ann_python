from datetime import datetime
import tensorflow as tf
D: float

class Neuron: # answer = True = ring | answer = False = pen
    def __init__(self, x, w, answer: bool, nreturn: bool):
        self.x = x
        self.w = w
        self.answer = answer
        self.nreturn = nreturn

    def ACTIVATE_THIS(self,
                    b: float) -> float:
        for i in range(0, len(self.x), 2):
            a = ((self.x[i] * self.w[i]) + (self.x[i + 1] * self.w[i + 1])) + b
            return a

    def TEACH_THIS(self, D, B, A, neuron1):
        i = 1
        file = open("aidata.txt", 'a')
        while neuron1.nreturn != neuron1.answer:
            if i == 1:
                A = ACTIVATE(neuron1, B)

                print(f'NEURON >> X: {self.x}')
                print(f'FIRST >> W: {self.w}, B: {B}')
                print(f'{i} >> {A}')

                if self.answer:
                    if A > 0:
                        self.nreturn = True
                    elif A < 0:
                        self.nreturn = False
                else:
                    if A < 0:
                        self.nreturn = False
                    elif A < 0:
                        self.nreturn = True

                if self.answer == self.nreturn:
                    if self.answer:
                        print("ring")
                        file.write('False /ring\n')
                    else:
                        print("pen")
                        file.write('True /pen\n')
                else:
                    print("...")

                LOG(self.x, self.w, B, A, self.nreturn, self.answer)
                print()
            else:
                is_positive = self.answer

                print(f'BEFORE >> W: {self.w}, B: {B}, IS_POSITIVE: {is_positive}')

                self.w = RETURN_NEW_W(D, self.w, self.x, is_positive)
                B = RETURN_NEW_B(D, B, is_positive)

                print(f'AFTER >> W: {self.w}, B: {B}, IS_POSITIVE: {is_positive}')
                A = ACTIVATE(neuron1, B)
                print(f'{i} >> {A}')

                if self.answer:
                    if A > 0:
                        self.nreturn = True
                    elif A < 0:
                        self.nreturn = False
                else:
                    if A < 0:
                        self.nreturn = False
                    elif A < 0:
                        self.nreturn = True

                if self.answer == self.nreturn:
                    if self.answer:
                        print("ring")
                        file.write('False /ring\n')
                    else:
                        print("pen")
                        file.write('True /pen\n')
                else:
                    print("...")

                LOG(self.x, self.w, B, A, self.nreturn, self.answer)
                print()
            i += 1
        file.write(f'{A} | {self.w} | {B} | {self.answer}\n')
        file.close()


class Model:  # --------------------------------------------------------------------------------------------------------
    def __int__(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10)
        ])

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


def LOG(x, w, b, a, nret, answ):
    file = open("aidata.txt", 'a')
    file.write('\n')
    file.write(str(datetime.now()))
    file.write(f'X: {x}')
    file.write(f'FIRST >> W: {w}\n')
    file.write(f'BEFORE >> W: {w}, B: {b}, IS_POSITIVE: {answ}\n')
    file.write(f'AFTER >> W: {w}, B: {b}, IS_POSITIVE: {answ}\n')
    file.write(f'>> {a}\n')
    file.write('\n')
    file.close()


def TEACH(D, B, A, neuron1: Neuron):
    i = 1
    file = open("aidata.txt", 'a')
    while neuron1.nreturn != neuron1.answer:
        if i == 1:
            A = ACTIVATE(neuron1, B)

            print(f'NEURON >> X: {neuron1.x}')
            print(f'FIRST >> W: {neuron1.w}, B: {B}')
            print(f'{i} >> {A}')

            if neuron1.answer:
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
                if neuron1.answer:
                    print("ring")
                    file.write('False /ring\n')
                else:
                    print("pen")
                    file.write('True /pen\n')
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

            if neuron1.answer:
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
                if neuron1.answer:
                    print("ring")
                    file.write('False /ring\n')
                else:
                    print("pen")
                    file.write('True /pen\n')
            else:
                print("...")

            LOG(neuron1.x, neuron1.w, B, A, neuron1.nreturn, neuron1.answer)
            print()
        i += 1
    file.write(f'{A} | {neuron1.w} | {B} | {neuron1.answer}\n')
    file.close()

def TEST_NEURON_SIMPLE_RP(B, A, neuron1: Neuron):
    COM = ""
    while COM != "end":
        print("com | com = any = start, com = end = end")
        COM = input("com :: ")
        if COM == "end":
            break
        else:
            X1 = float(input("x1 [o-y]: "))
            X2 = float(input("x2 [o-x]: "))
            TEMP_X = [X1, X2]

            neuron2 = Neuron([X1, X2], neuron1.w, False, not False)
            A = ACTIVATE(neuron2, B)
            LOG(TEMP_X, neuron1.w, B, A, False, not False)

            if A > 0:
                print("False / ring")
            else:
                print("True / pen")
