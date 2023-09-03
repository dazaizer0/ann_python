import AILib as AL

B = 6
D = 0.01
A = 0

network = AL.Network([[AL.Neuron([1, 2], [3, 4], False, True),
                      AL.Neuron([5, 6], [7, 8], False, True)],
                      [AL.Neuron([9, 8], [7, 6], True, False)]
                      ], 2)

network.ACTIVATE_THIS_NETWORK()
