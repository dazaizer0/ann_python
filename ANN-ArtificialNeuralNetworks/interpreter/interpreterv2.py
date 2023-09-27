import time
import AILib as ai
import AIDataReader as reader
import lib_rs as rs


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


def do_it(data):

    data_len = len(data)
    rep = data[data_len - 2]
    show_time = False

    variables = {
        "ret": data[data_len - 2],
    }
    fns = {

    }

    if data[data_len - 3] == "rep":
        start_time = time.time()
        for r in range(int(rep)):
            for i in range(len(data)):
                # mod start
                if data[i] == "mod" and data[i + 2] == "[":
                    j = i
                    while data[j] != "]start":
                        # show start
                        if data[j] == "show" and data[j + 2] == ";":
                            if data[j + 1] == "dur":
                                show_time = True
                        # show end
                        j += 1
                    fns[data[i + 1]] = data[i + 3]
                # mod end
                # math start
                if data[i] in variables.keys():
                    # sum
                    if data[i + 1] == "+=":
                        temp: int

                        if data[i + 3] == "rep()":
                            try:
                                temp: int = rs.sum(int(variables[data[i]].var), (int(variables[data[i + 2]].var) * int(rep)))
                            except:
                                temp: int = rs.sum(int(variables[data[i]].var), (int(data[i + 2]) * int(rep)))
                        else:
                            try:
                                temp: int = rs.sum(int(variables[data[i]].var), int(variables[data[i + 2]].var))
                            except:
                                temp: int = rs.sum(int(variables[data[i]].var), int(data[i + 2]))

                        variables[data[i]].var = temp
                    # sub
                    if data[i + 1] == "-=":
                        temp: int
                        if data[i + 3] == "rep()":
                            try:
                                temp: int = rs.sub(int(variables[data[i]].var),
                                                   (int(variables[data[i + 2]].var) * int(rep)))
                            except:
                                temp: int = rs.sub(int(variables[data[i]].var), (int(data[i + 2]) * int(rep)))
                        else:
                            try:
                                temp: int = rs.sub(int(variables[data[i]].var), int(variables[data[i + 2]].var))
                            except:
                                temp: int = rs.sub(int(variables[data[i]].var), int(data[i + 2]))

                        variables[data[i]].var = temp
                    # mul
                    if data[i + 1] == "*=":
                        temp: int
                        if data[i + 3] == "rep()":
                            try:
                                temp: int = rs.mul(int(variables[data[i]].var),
                                                   (int(variables[data[i + 2]].var) * int(rep)))
                            except:
                                temp: int = rs.mul(int(variables[data[i]].var), (int(data[i + 2]) * int(rep)))
                        else:
                            try:
                                temp: int = rs.mul(int(variables[data[i]].var), int(variables[data[i + 2]].var))
                            except:
                                temp: int = rs.mul(int(variables[data[i]].var), int(data[i + 2]))

                        variables[data[i]].var = temp
                    # div
                    if data[i + 1] == "/=":
                        temp: float = 0.0
                        if data[i + 3] == "rep()":
                            try:
                                temp = float(variables[data[i]].var) / float(variables[data[i + 2]].var) * int(rep)
                            except:
                                temp = float(variables[data[i]].var) / float(data[i + 2]) * int(rep)
                        else:
                            try:
                                temp = float(variables[data[i]].var) / float(variables[data[i + 2]].var)
                            except:
                                temp = float(variables[data[i]].var) / float(data[i + 2])

                            variables[data[i]].var = temp
                # math end
                # variables start
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
                # variables end
                # loop start
                if data[i] == "loop":
                    j = i
                    todo = []
                    while_value: int = int(data[i + 1])
                    while data[j] != "]start":
                        todo.append(data[j])
                        j += 1

                    k = 0
                    for i in range(while_value):
                        do_it(todo)
                        k += 1
                # loop end
                # ailib functions start
                if data[i] == "new":
                    if data[i + 1] == "2val_lists":
                        ai.GEN_2VAL_LISTS_ANSWERS(int(data[i + 2]), list(data[i + 3]), list(data[i + 4]))
                # ailib functions end
                # out start
                if data[i] == "out":
                    if data[i + 1] in variables.keys():
                        print(variables[data[i + 1]])
                    else:
                        j = i + 1
                        output = ""
                        while data[j] != ";":
                            try:
                                if data[j] == "/n":
                                    data[j] = ""
                                    print()
                                temp: int = int(data[j])
                                char = chr(temp)
                                output += char
                            except:
                                output += data[j]
                            j += 1
                        print(output, end="")

                # out end
        end_time = time.time()
        if show_time:
            print(end_time - start_time)


do_it(data)
