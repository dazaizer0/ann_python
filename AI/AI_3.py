import AI_2 as AI

AI.D = 0.001
A = 0

x_totrain = []
answ_totrain = []

AI.GEN_2V_DATA_LIST(10, x_totrain, answ_totrain)
print(x_totrain)
print(answ_totrain)

n = AI.Neuron([45, 21], [2, -4], False, not False)

n.LOG_THIS(AI.CB)
for i in range(0, len(x_totrain)):
    n = AI.Neuron(x_totrain[i], [2, -4], bool(answ_totrain[i]), not bool(answ_totrain[i]))
    AI.TEACH(AI.D, AI.CB, A, n)

n.LOG_THIS(AI.CB)
AI.TEST_NEURON_SIMPLE_RP(AI.CB, A, n)
