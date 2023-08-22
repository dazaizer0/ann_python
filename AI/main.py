class Neuron:
    def __init__(self, x1, x2, w1, w2):
        self.x1 = x1
        self.w1 = w1
        self.x2 = x2
        self.w2 = w2


def activate(n: Neuron, b):
    a = ((n.x1 * n.w1) + (n.x2 * n.w2)) + b
    return a


const_d = 0.2
bias = 6

neuron1 = Neuron(23, 4, -2, 0.1)
neuron2 = Neuron(18, 7, -2, 0.1)
a1 = activate(neuron1, bias)
a2 = activate(neuron2, bias)

neuron3 = Neuron(a1, a2, -2, 0.1)
a3 = activate(neuron3, bias)
print(a3)

'''neuron.w1 = neuron.w1 + (neuron.x1 * const_d * 1)
neuron.w2 = neuron.w2 + (neuron.x2 * const_d * 1)
bias = bias + 1 * const_d
print(f'{i} >>> a: {a} >>> x1: {neuron.x1}, x2: {neuron.x2}, w1: {neuron.w1}, w2: {neuron.w2}')'''
