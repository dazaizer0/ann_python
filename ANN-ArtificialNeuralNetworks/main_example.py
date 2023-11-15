import AILib as AL
import AIDataReader as adr


B = 6
D = 0.01
A = 0

xtrain: list = []
answers: list = []

reader = adr.AIDataReader('data/aidata.txt')
print(reader)

AL.GEN_2VAL_LISTS_ANSWERS(200, xtrain, answers)
print(xtrain)
print(answers)

neuron_w = [-2, 0.1]
n1 = AL.Neuron([1, 0], neuron_w, False, True)
mode = AL.Mode(False, 0, A, n1.nreturn)

for i in range(0, len(xtrain)):
    n1 = AL.Neuron(xtrain[i], neuron_w, bool(answers[i]), not bool(answers[i]))
    n1.TRAIN_NEURON(A, B, D, mode)
    neuron_w = n1.w

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

        n2 = AL.Neuron([X1, X2], n1.w, False, not False)
        print(n1)

        a_Result = n2.ACTIVATE(B)

        AL.LOG_OTHER(TEMP_X, n1.w, B, a_Result, False, not False, 'data/aidata.txt')

        if a_Result > 0:
            print(f'False / RING, A: {a_Result}')
        else:
            print(f'True / PEN, A: {a_Result}')

