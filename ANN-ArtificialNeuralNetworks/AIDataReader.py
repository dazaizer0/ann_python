import time

class AIDataReader:
    def __init__(self, data_file_name):
        self.data_file_name = data_file_name

    def __repr__(self):
        f = open(self.data_file_name, 'r')
        data = f.readlines()
        f.close()

        return str(data)

    def READ_AS_LIST(self):
        f = open(self.data_file_name, 'r')
        data = f.readlines()
        f.close()

        return data
