import random
from datetime import datetime
import random

class Mode:
    def __init__(self, mode, const_float, number, nreturn):
        self.mode = mode
        self.const_float = const_float
        self.number = number
        self.nreturn = nreturn

    def SET_MODE_MOL(self):
        if self.mode == False:
            if self.number > self.const_float:
                self.nreturn = False
            else:
                self.nreturn = True
        else:
            if self.number < self.const_float:
                self.nreturn = False
            else:
                self.nreturn = True

        return self.nreturn

    def SET_MODE_ND(self):
        return abs(self.const_float - self.number)

class Neuron:
    def __init__(self, x, w, answer: bool, nreturn: bool):
        self.x = x
        self.w = w
        self.answer = answer
        self.nreturn = nreturn

    def __repr__(self):
        return f'x: {self.x}, w: {self.w}, answer: {self.answer}, nreturn: {self.nreturn}'

    def LOG_DATA(self, a_result, b_Bias, file_name):
        file = open(file_name, 'a')
        file.write(f'{str(datetime.now())} >> X: {self.x}, W: {self.w},B: {b_Bias}, answer: {self.answer}, nreturn: {self.nreturn}, A: {a_result}\n')
        file.close()

    def ACTIVATE(self,
                    Bias: float) -> float:
        for i in range(0, len(self.x), 2):
            a = ((self.x[i] * self.w[i]) + (self.x[i + 1] * self.w[i + 1])) + Bias
            return a

    def TRAIN_NEURON(self, a_Result, b_Bias, d_Accuracy, mode_rules: Mode):
        i = 1
        while self.nreturn != self.answer:
            if i == 1:

                a_Result = self.ACTIVATE(b_Bias)
                print(f'{i} >> n >> {self}')
                print(f'{i} >> {a_Result}')

                mode = Mode(mode_rules.mode, mode_rules.const_float, a_Result, self.nreturn)
                self.nreturn = mode.SET_MODE_MOL()

                if self.answer == self.nreturn:
                    if self.answer:
                        print("pen")
                    else:
                        print("ring")

                else:
                    if self.answer:
                        print("wrong = ring")
                    else:
                        print("wrong = pen")
            else:

                print(f'BEF >> W: {self.w}, B: {b_Bias}, nreturn: {self.nreturn}, X: {self.x}')

                self.w = RETURN_NEW_W(d_Accuracy, self.w, self.x, self.answer)
                b_Bias = RETURN_NEW_B(d_Accuracy, b_Bias, self.answer)

                print(f'AFT >> W: {self.w}, B: {b_Bias}, nreturn: {self.nreturn}, X: {self.x}')
                a_Result = self.ACTIVATE(b_Bias)
                print(f'{i} >> {a_Result} = ', end="")

                mode = Mode(mode_rules.mode, mode_rules.const_float, a_Result, self.nreturn)
                self.nreturn = mode.SET_MODE_MOL()

                if self.answer == self.nreturn:
                    if self.answer:
                        print("pen")
                    else:
                        print("ring")

                else:
                    if self.answer:
                        print("wrong = ring")
                    else:
                        print("wrong = pen")

                self.LOG_DATA(a_Result, b_Bias, 'data/aidata.txt')
                print()
            i += 1

def RETURN_TRANSFERRED_DATA(from_neuron1: Neuron, from_neuron2: Neuron, to_neuron: Neuron, B):
    A1 = from_neuron1.ACTIVATE(B)
    A2 = from_neuron2.ACTIVATE(B)

    to_neuron.x = [A1, A2]
    return to_neuron.ACTIVATE(B)

class Network:  # IN DEVELOPMENT
    def __init__(self, neuron_list: list, layers: int):
        self.neuron_list = neuron_list
        self.layers = layers

    def ACTIVAT(self):
        for i1, neuron_layer in enumerate(self.neuron_list):
            for i2, neuron in enumerate(neuron_layer):
                print(f'{i1}/{i2} >> {neuron}')

def LOG_OTHER(neuron_x, neuron_w, b_Bias, a_Result, nreturn, answer, file_name):
    file = open(file_name, 'a')
    file.write(f'{str(datetime.now())} - LOG_O - X: {neuron_x}, W: {neuron_w}, B: {b_Bias}, nreturn: {nreturn}, answer: {answer}, A: {a_Result}\n')
    file.close()
def RETURN_NEW_W(d_Accuracy, neuron_w, neuron_x, answer: bool):
    if answer:
        for i in range(0, len(neuron_w)):
            neuron_w[i] = neuron_w[i] + neuron_x[i] * d_Accuracy * -1
    else:
        for i in range(0, len(neuron_w)):
            neuron_w[i] = neuron_w[i] + neuron_x[i] * d_Accuracy * 1

    return neuron_w

def RETURN_NEW_B(d_Accuracy, b_Bias, answer: bool):
    if answer:
        return b_Bias + -1 * d_Accuracy
    else:
        return b_Bias + 1 * d_Accuracy

def GEN_2VAL_LIST(short_temp):
    while short_temp[0] == short_temp[1]:
        short_temp = [random.randint(5, 100), random.randint(5, 100)]
    return short_temp

def GEN_2VAL_LISTS_ANSWERS(number_of_lists, x_list: list, answer_list: list):
    for i in range(0, number_of_lists):
        short_temp = [0, 0]
        short_temp = GEN_2VAL_LIST(short_temp)

        if short_temp[0] > short_temp[1]:
            answer_list.append(False)
        else:
            answer_list.append(True)
        x_list.append(short_temp)
