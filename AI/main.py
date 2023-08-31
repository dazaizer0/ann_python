import AI_2 as AI
from random import randint

AI.D = 0.0001
B = 4
A = 0

neuron1 = AI.Neuron([45, 14], [2, 3], True, not True)

AI.TEACH(AI.D, B, A, neuron1)
AI.TEST_NEURON_SIMPLE_RP(B, A, neuron1)
