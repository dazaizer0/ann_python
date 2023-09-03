import random
from datetime import datetime
import tensorflow as tf
import random
D: float
CB = 6.0

class Neuron:  # answer = False = ring | answer = True = pen
    def __init__(self, x, w, answer: bool, nreturn: bool):
        self.x = x
        self.w = w
        self.answer = answer
        self.nreturn = nreturn

    def __repr__(self):
        return f'x: {self.x}, w: {self.w}, answer: {self.answer}, nreturn: {self.nreturn}'

    def LOG_TO_FILE(self, A, file_name):
        file = open(file_name, 'a')
        file.write(f'{str(datetime.now())} - LOG >> X: {self.x}, W: {self.w}, answer: {self.answer}, nreturn: {self.nreturn}, A: {A}\n')
        file.close()

    def ACTIVATE_THIS(self,
                    b: float) -> float:
        for i in range(0, len(self.x), 2):
            a = ((self.x[i] * self.w[i]) + (self.x[i + 1] * self.w[i + 1])) + b
            return a

    def TEACH(self, D, B, A):
        i = 1
        while self.nreturn != self.answer:
            if i == 1:
                A = ACTIVATE(self, B)

                print(f'NEURON >> X: {self.x}')
                print(f'FIRST >> W: {self.w}, B: {B}')
                print(f'{i} >> {A}')

                if self.answer:
                    if A > 0:
                        self.nreturn = False
                    elif A < 0:
                        self.nreturn = True
                else:
                    if A < 0:
                        self.nreturn = False
                    elif A > 0:
                        self.nreturn = True

                if self.answer == self.nreturn:
                    if self.answer:
                        print("ring")
                    else:
                        print("pen")
                else:
                    print("...")

                self.LOG_TO_FILE(A, 'aidata.txt')
                print()
            else:
                is_positive = self.answer

                print(f'BEFORE >> W: {self.w}, B: {B}, IS_POSITIVE: {is_positive}')

                self.w = RETURN_NEW_W(D, self.w, self.x, is_positive)
                B = RETURN_NEW_B(D, B, is_positive)

                print(f'AFTER >> W: {self.w}, B: {B}, IS_POSITIVE: {is_positive}')
                A = ACTIVATE(self, B)
                print(f'{i} >> {A}')

                if self.answer:
                    if A > 0:
                        self.nreturn = False
                    elif A < 0:
                        self.nreturn = True
                else:
                    if A > 0:
                        self.nreturn = False
                    elif A < 0:
                        self.nreturn = True

                if self.answer == self.nreturn:
                    if self.answer:
                        print("ring")
                    else:
                        print("pen")
                else:
                    print("...")

                self.LOG_TO_FILE(A, 'aidata.txt')
                print()
            i += 1

class NeuronNetwork:
    def __init__(self, Neuron1: Neuron, Neuron2: Neuron, D: float, B: float):
        self.Neuron1 = Neuron1
        self.Neuron2 = Neuron2
        self.D = D
        self.B = B

    def GET_RESULT(self, loops: int):
        for i in range(0, loops):
            a1 = ACTIVATE(self.Neuron1, self.B)
            a2 = ACTIVATE(self.Neuron2, self.B)

            CHOICE1 = CHECK_NRETURN(self.Neuron1)
            CHOICE2 = CHECK_NRETURN(self.Neuron2)

            if CHOICE1 == True and CHOICE2 == False:
                self.B = RETURN_NEW_B(self.D, self.B, self.Neuron2.nreturn)
                self.Neuron2.w = RETURN_NEW_W(self.D, self.Neuron2.x, self.Neuron2.w, self.Neuron2.answer)
                print(f'a1: {a1}, a2: {a2}')
            elif CHOICE1 == False and CHOICE2 == True:
                self.B = RETURN_NEW_B(self.D, self.B, self.Neuron1.nreturn)
                self.Neuron1.w = RETURN_NEW_W(self.D, self.Neuron1.x, self.Neuron1.w, self.Neuron1.answer)
                print(f'a1: {a1}, a2: {a2}')
            elif CHOICE1 == False and CHOICE2 == False:
                self.B = RETURN_NEW_B(self.D, self.B, self.Neuron1.nreturn)
                self.Neuron1.w = RETURN_NEW_W(self.D, self.Neuron1.x, self.Neuron1.w, self.Neuron1.answer)
                print(f'a1: {a1}, a2: {a2}')
            else:
                break

def LOG_OTHER(x, w, b, a, nret, answ, file_name):
    file = open(file_name, 'a')
    file.write(f'{str(datetime.now())} - LOG_O - X: {x}, W: {w}, B: {b}, nreturn: {nret}, answer: {answ}, A: {a}\n')
    file.close()

def CHECK_NRETURN(n: Neuron):
    if n.nreturn:
        return n.answer
    else:
        return not n.answer

def ACTIVATE(n: Neuron,
             b: float) -> float:
    for i in range(0, len(n.x), 2):
        a = ((n.x[i] * n.w[i]) + (n.x[i + 1] * n.w[i + 1])) + b
        return a


def RETURN_NEW_W(d, w, x, is_positive: bool):
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

def TEST_NEURON_SIMPLE_RP(B, A, neuron1: Neuron):
    COM = ""
    while COM != "end":
        print("com | com = any = start, com = end = end")
        COM = input("com :: ")
        if COM == "end":
            break
        else:
            X1 = float(input("x1 [o-y][mm]: "))
            X2 = float(input("x2 [o-x][mm]: "))
            TEMP_X = [X1, X2]

            neuron2 = Neuron([X1, X2], neuron1.w, False, not False)
            A = ACTIVATE(neuron2, B)
            LOG_OTHER(TEMP_X, neuron1.w, B, A, False, not False, 'aidata.txt')

            if A > 0:
                print("False / ring")
            else:
                print("True / pen")

def GEN_SHORT2V_LIST(short_temp):
    while short_temp[0] == short_temp[1]:
        short_temp = [random.randint(5, 100), random.randint(5, 100)]
    return short_temp

# answer = False = ring | answer = True = pen
def GEN_2V_DATA_LIST(number_of_lists, x_list: list, answer_list: list):
    for i in range(0, number_of_lists):
        short_temp = [0, 0]
        short_temp = GEN_SHORT2V_LIST(short_temp)

        if short_temp[0] > short_temp[1]:
            answer_list.append(False)
        else:
            answer_list.append(True)
        x_list.append(short_temp)

