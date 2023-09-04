import random
from datetime import datetime
import random

class Neuron: # answer = True = ring | answer = False = pen
    def __init__(self, x, w, answer: bool, nreturn: bool):
        self.x = x
        self.w = w
        self.answer = answer
        self.nreturn = nreturn

    def __repr__(self):
        return f'x: {self.x}, w: {self.w}, answer: {self.answer}, nreturn: {self.nreturn}'

    def LOG_TO_FILE(self, a_result, b_Bias, file_name):
        file = open(file_name, 'a')
        file.write(f'{str(datetime.now())} >> X: {self.x}, W: {self.w},B: {b_Bias}, answer: {self.answer}, nreturn: {self.nreturn}, A: {a_result}\n')
        file.close()

    def ACTIVATE_THIS(self,
                    Bias: float) -> float:
        for i in range(0, len(self.x), 2):
            a = ((self.x[i] * self.w[i]) + (self.x[i + 1] * self.w[i + 1])) + Bias
            return a

    def FIT(self, a_Result, b_Bias, d_Accuracy):
        i = 1
        while self.nreturn != self.answer:
            if i == 1:

                a_Result = self.ACTIVATE_THIS(b_Bias)
                print(f'{i} >> n >> {self}')
                print(f'{i} >> {a_Result}')

                if a_Result > 0:
                    self.nreturn = False  # ring
                else:
                    self.nreturn = True  # pen

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
                a_Result = self.ACTIVATE_THIS(b_Bias)
                print(f'{i} >> {a_Result} = ', end="")

                if a_Result > 0:
                    self.nreturn = False  # ring
                else:
                    self.nreturn = True  # pen

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

                self.LOG_TO_FILE(a_Result,b_Bias, 'aidata.txt')
                print()
            i += 1

def GET_TRANSFERRED_DATA(from_neuron1: Neuron, from_neuron2: Neuron, to_neuron: Neuron, B):
    A1 = from_neuron1.ACTIVATE_THIS(B)
    A2 = from_neuron2.ACTIVATE_THIS(B)

    to_neuron.x = [A1, A2]
    return to_neuron.ACTIVATE_THIS(B)

class Network:  # IN DEVELOPMENT
    def __init__(self, neuron_list: list, layers: int):
        self.neuron_list = neuron_list
        self.layers = layers

    def ACTIVATE_THIS_NETWORK(self):
        for i1, neuron_layer in enumerate(self.neuron_list):
            for i2, neuron in enumerate(neuron_layer):
                print(f'{i1}/{i2} >> {neuron}')

def LOG_OTHER(neuron_x, neuron_w, b_Bias, a_Result, nreturn, answer, file_name):
    file = open(file_name, 'a')
    file.write(f'{str(datetime.now())} - LOG_O - X: {neuron_x}, W: {neuron_w}, B: {b_Bias}, nreturn: {nreturn}, answer: {answer}, A: {a_Result}\n')
    file.close()

def CHECK_NRETURN(n: Neuron):
    if n.nreturn:
        return n.answer
    else:
        return not n.answer

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

def TEST_NEURON_SIMPLE_RP(b_Bias, a_Result, n: Neuron):
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

            n2 = Neuron([X1, X2], n.w, False, not False)
            print(n)

            a_Result = n2.ACTIVATE_THIS(b_Bias)

            LOG_OTHER(TEMP_X, n.w, b_Bias, a_Result, False, not False, 'aidata.txt')

            if a_Result > 0:
                print(f'False / ring, A: {a_Result}')
            else:
                print(f'True / pen, A: {a_Result}')

def GEN_SHORT2V_LIST(short_temp):
    while short_temp[0] == short_temp[1]:
        short_temp = [random.randint(5, 100), random.randint(5, 100)]
    return short_temp

def GEN_2V_DATA_LIST(number_of_lists, x_list: list, answer_list: list):
    for i in range(0, number_of_lists):
        short_temp = [0, 0]
        short_temp = GEN_SHORT2V_LIST(short_temp)

        if short_temp[0] > short_temp[1]:
            answer_list.append(False)
        else:
            answer_list.append(True)
        x_list.append(short_temp)