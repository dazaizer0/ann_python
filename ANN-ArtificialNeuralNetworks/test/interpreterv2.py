file = open("main.txt", 'r')

data = file.read()
data = data.replace('\n', '')
data = data.replace(';', ' ;')
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

if data[data_len - 3] == "return":
    for r in range(int(rep)):
        for i in range(len(data)):
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
