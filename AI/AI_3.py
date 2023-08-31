import tensorflow as tf
import AI_2 as AI

B = 6
D = 0.001
A = 0
n = AI.Neuron([24, 45], [4, -1], True, not True)
n.ACTIVATE_THIS(B)
n.TEACH_THIS(D, B, A, n)
