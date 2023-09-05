#  soon
from bottle import Bottle, request, template
import AILib as AL

B = 6
D = 0.01
A = 0

xtrain: list = []
answers: list = []


AL.GEN_2VAL_LISTS_ANSWERS(200, xtrain, answers)

neuron_w = [-2, 0.1]
neuron = AL.Neuron([1, 0], neuron_w, False, True)
mode = AL.Mode(False, 0, A, neuron.nreturn)


for i in range(0, len(xtrain)):
    neuron = AL.Neuron(xtrain[i], neuron_w, bool(answers[i]), not bool(answers[i]))
    neuron.TRAIN_NEURON(A, B, D, mode)
    neuron_w = neuron.w

#  WEB
app = Bottle()

@app.route('/')
def index():
    return template('web/index.html')

@app.route('/submit', method='POST')
def submit():
    data = request.forms.get('data')
    elements = data.split(",")
    x_values = [int(element) for element in elements]

    neuron.x = x_values
    A = neuron.ACTIVATE(B)
    if A > 0:
        return f'{x_values[0]}mm, {x_values[1]}mm >> This is RING, A: {A}'
    else:
        return f'{x_values[0]}mm, {x_values[1]}mm >> This is PEN, A: {A}'


if __name__ == '__main__':
    app.run(host='localhost', port=5104)
