import AI_2 as AI

AI.D = 0.001
A = 0

n = AI.Neuron([24, 45],
              [4, -1],
              True, not True)

n1 = AI.Neuron([456, 123],
               [2, 1],
               False, not False)

tn1 = AI.datetime.now()
nn1 = AI.NeuronNetwork(n, n1, AI.D, AI.B)
nn1.GET_RESULT(10)
tn2 = AI.datetime.now()
td = tn1 - tn2
print(f'nn time duration: {td}')
