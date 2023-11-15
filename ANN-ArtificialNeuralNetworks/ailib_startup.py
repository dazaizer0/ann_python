import AILib as AL


B = 6
D = 0.01
A = 0

xtrain: list = []
answers: list = []

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
