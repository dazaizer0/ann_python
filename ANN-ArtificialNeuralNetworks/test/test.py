class var:
    def __init__(self, var_type, value):
        self.var_type = var_type
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __sub__(self, other):
        return self.value + other


vars = [var(int, 0), ]

file = open('test.txt', 'r')
data = file.read()
data = data.split(';')

for i in data:
    i.replace('\n', '')

for i in range(len(data)):
    if data[i] == "cvar":
        temp_var = var(str(data[i + 1]), data[i + 2])
        vars.append(temp_var)

    if data[i] == "out":
        if data[i + 1] == "var":
            nr = int(data[i + 2])
            print(vars[nr])
        if data[i + 1] == "sum":
            if data[i + 2] == "var":
                what = data[i + 2]
                sum = 0
                for l in range(len(what)):
                    var_list = []
                    try:
                        var_list.append(int(vars[l].value))
                    except:
                        continue
                    for nr in var_list:
                        sum += nr
                print(sum)
            else:
                what = data[i + 2]
                sum = 0
                for l in what:
                    try:
                        l = int(l)
                    except:
                        continue
                    if i != "+":
                        sum += l
                print(sum)
