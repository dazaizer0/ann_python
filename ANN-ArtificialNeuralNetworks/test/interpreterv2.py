file = open("main.txt", 'r')

data = file.read()
data = data.replace('\n', '')
data = data.replace(';', ' ;')
data = data.split(' ')

for i in range(len(data)):
    if data[i] == "out":
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
