import AILib as AL

B = 6
D = 0.01
A = 0

xtrain: list = []
answertrain: list = []

AL.GEN_2V_DATA_LIST(200, xtrain, answertrain)
print(xtrain)
print(answertrain)

neuron_w = [-2, 0.1]
n1 = AL.Neuron([1, 0], neuron_w, False, True)

for i in range(0, len(xtrain)):
    n1 = AL.Neuron(xtrain[i], neuron_w, bool(answertrain[i]), not bool(answertrain[i]))
    n1.FIT(A, B, D)
    neuron_w = n1.w

AL.TEST_NEURON_SIMPLE_RP(B, A, n1)
