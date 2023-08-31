import AI_2 as AI

D = 0.0001
B = 4
A = 0

neuron1 = AI.Neuron([18, 34], [2, 3], False, not False)
AI.TEACH(D, B, A, neuron1)

COM = ""
while COM != "end":
    print("com | com = any = start, com = end = end")
    COM = input("com :: ")
    if COM == "end":
        break
    else:
        X1 = float(input("x1 [o-y]: "))
        X2 = float(input("x2 [o-x]: "))
        TEMP_X = [X1, X2]

        neuron2 = AI.Neuron([X1, X2], neuron1.w, False, not False)
        A = AI.ACTIVATE(neuron2, B)
        AI.LOG(TEMP_X, neuron1.w, B, A, False, not False)

        if A > 0:
            print("False / Obraczka")
        else:
            print("True / Dlugopis")
