import time
import AILib as ai
import AIDataReader as reader


file = open("main.txt", 'r')

data = file.read()
data = data.replace('\n', '')
data = data.replace(';', ' ;')
data = data.replace(',', ' , ')
data = data.replace('->', ' ')
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

fns = {

}

data_len = len(data)
rep = data[data_len - 2]
show_time = False

if data[data_len - 3] == "return":
    start_time = time.time()
    for r in range(int(rep)):
        for i in range(len(data)):
            if data[i] == "mod" and data[i + 2] == "[":
                j = i
                while data[j] != "]start":
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
                                temp: float = float(variables[data[i]].var) / float(variables[data[i + 2]].var)
                            except:
                                temp: float = float(variables[data[i]].var) / float(data[i + 2])
                            try:
                                temp = int(temp)
                                variables[data[i]].var = temp
                            except:
                                continue

                    if data[i] == "cre" and data[i + 4] == ";":
                        if data[i + 1] == "listint":
                            that_list: list
                            try:
                                that_list = data[i + 3].split('.')

                                for l in range(len(that_list)):
                                    that_list[l] = int(that_list[l])

                                temp: variable = variable(data[i + 1], that_list)
                                variables[data[i + 2]] = temp
                            except:
                                that_list = []

                        elif data[i + 1] == "listbool":
                            that_list: list
                            try:
                                that_list = data[i + 3].split('.')

                                for l in range(len(that_list)):
                                    if that_list[l] == "true":
                                        that_list[l] = bool(True)
                                    else:
                                        that_list[l] = bool(False)
                            except:
                                that_list = []

                            temp: variable = variable(data[i + 1], that_list)
                            variables[data[i + 2]] = temp

                        else:
                            temp: variable = variable(data[i + 1], data[i + 3])
                            variables[data[i + 2]] = temp

                    j += 1
                fns[data[i + 1]] = data[i + 3]
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
                        temp: float = float(variables[data[i]].var) / float(variables[data[i + 2]].var)
                    except:
                        temp: float = float(variables[data[i]].var) / float(data[i + 2])
                    try:
                        temp = int(temp)
                        variables[data[i]].var = temp
                    except:
                        continue

            if data[i] == "cre" and data[i + 4] == ";":
                if data[i + 1] == "listint":
                    that_list: list
                    try:
                        that_list = data[i + 3].split('.')

                        for l in range(len(that_list)):
                            that_list[l] = int(that_list[l])

                        temp: variable = variable(data[i + 1], that_list)
                        variables[data[i + 2]] = temp
                    except:
                        that_list = []

                elif data[i + 1] == "listbool":
                    that_list: list
                    try:
                        that_list = data[i + 3].split('.')

                        for l in range(len(that_list)):
                            if that_list[l] == "true":
                                that_list[l] = bool(True)
                            else:
                                that_list[l] = bool(False)
                    except:
                        that_list = []

                    temp: variable = variable(data[i + 1], that_list)
                    variables[data[i + 2]] = temp

                else:
                    temp: variable = variable(data[i + 1], data[i + 3])
                    variables[data[i + 2]] = temp

            if data[i] == "new":
                if data[i + 1] == "2val_lists":
                    ai.GEN_2VAL_LISTS_ANSWERS(int(data[i + 2]), list(data[i + 3]), list(data[i + 4]))

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
