import time


file = open("main.txt", 'r')

data = file.read()
data = data.replace('\n', '')
data = data.replace(';', ' ;')
data = data.replace(',', ' , ')
data = data.split(' ')

class variable:
    def __init__(self, typ, var):
        self.typ = typ

        if typ == "int":
            self.var = int(var)
        if typ == "str":
            self.var = str(var)
        else:
            self.var = var

    def __repr__(self):
        return str(self.var)


variables = {

}

data_len = len(data)
rep = data[data_len - 2]
show_time = False

if data[data_len - 3] == "return":
    start_time = time.time()
    for r in range(int(rep)):
        for i in range(len(data)):
            if data[i] == "show" and data[i + 2] == ";":
                if data[i + 1] == "dur":
                    show_time = True
            if data[i] in variables.keys():
                if data[i + 1] == "+=":
                    try:
                        temp: int = int(variables[data[i]].var) + int(variables[data[i + 2]].var)
                    except:
                        temp: int = int(variables[data[i]].var) + int(data[i + 2])
                    variables[data[i]].var = temp
                if data[i + 1] == "-=":
                    try:
                        temp: int = int(variables[data[i]].var) - int(variables[data[i + 2]].var)
                    except:
                        temp: int = int(variables[data[i]].var) - int(data[i + 2])
                    variables[data[i]].var = temp
                if data[i + 1] == "*=":
                    try:
                        temp: int = int(variables[data[i]].var) * int(variables[data[i + 2]].var)
                    except:
                        temp: int = int(variables[data[i]].var) * int(data[i + 2])
                    variables[data[i]].var = temp
                if data[i + 1] == "/=":
                    try:
                        temp: int = int(variables[data[i]].var) / int(variables[data[i + 2]].var)
                    except:
                        temp: int = int(variables[data[i]].var) / int(data[i + 2])
                    try:
                        temp = int(temp)
                        variables[data[i]].var = temp
                    except:
                        continue

            if data[i] == "cre" and data[i + 4] == ";":
                temp: variable = variable(data[i + 1], data[i + 3])
                variables[data[i + 2]] = temp

            if data[i] == "out":
                if data[i + 1] in variables.keys():
                    print(variables[data[i + 1]])
                else:
                    j = i + 1
                    output = ""
                    while data[j] != ";":
                        try:
                            temp: int = int(data[j])
                            char = chr(temp)
                            output += char
                        except:
                            output += "-"
                        j += 1
                    print(output)
    end_time = time.time()
    if show_time:
        print(end_time - start_time)
