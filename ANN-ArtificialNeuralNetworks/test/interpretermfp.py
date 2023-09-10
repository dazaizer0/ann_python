class var:
    def __init__(self, var_type, value):
        self.var_type = var_type
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __sub__(self, other):
        return self.value + other

    def type(self):
        print(self.var_type)

def out(what):
    print(what)

direction = input("direction: ")
vars = {"zero": var(int, 0), }

try:
    file = open(direction, 'r')
    data = file.read()
    data = data.replace('\n', '')
    data = data.replace(' ', ';')
    data = data.split(';')

    for i in data:
        i.replace('\n', '')

    for i in range(len(data)):
        # create variable
        if data[i] == "cvar":
            temp_var = var(str(data[i + 1]), data[i + 2])
            vars[data[i + 3]] = temp_var

        # add variables
        if data[i] == "oper":
            if data[i + 1] == "var+":
                if vars[data[i + 2]].var_type == "int":
                    b = int(vars[data[i + 3]].value)
                    c = int(vars[data[i + 4]].value)
                    vars[data[i + 2]].value = b + c
                else:
                    vars[data[i + 2]].value = vars[data[i + 3]].value + vars[data[i + 4]].value

            if data[i + 1] == "var-":
                if vars[data[i + 2]].var_type == "int":
                    b = int(vars[data[i + 3]].value)
                    c = int(vars[data[i + 4]].value)
                    vars[data[i + 2]].value = b - c
                else:
                    vars[data[i + 2]].value = vars[data[i + 3]].value - vars[data[i + 4]].value

            if data[i + 1] == "var*":
                if vars[data[i + 2]].var_type == "int":
                    b = int(vars[data[i + 3]].value)
                    c = int(vars[data[i + 4]].value)
                    vars[data[i + 2]].value = b * c
                else:
                    vars[data[i + 2]].value = vars[data[i + 3]].value * vars[data[i + 4]].value

            if data[i + 1] == "var/":
                if vars[data[i + 2]].var_type == "int":
                    b = int(vars[data[i + 3]].value)
                    c = int(vars[data[i + 4]].value)
                    vars[data[i + 2]].value = b * c
                else:
                    vars[data[i + 2]].value = vars[data[i + 3]].value / vars[data[i + 4]].value


        # show variables
        if data[i] == "vars":
            out(vars)

        # out
        if data[i] == "out":
            if data[i + 1] == "var":
                out(vars[data[i + 2]])
            else:
                out(data[i + 1])

except:
    print("not found")
