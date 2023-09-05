import time

class AIDataReader:
    def __init__(self, data_file_name):
        """
        AIDataReader allows you to receive and process data collected from the operation of neurons
        :param data_file_name:
        """
        self.data_file_name = data_file_name

    def __repr__(self):
        f = open(self.data_file_name, 'r')
        data = f.readlines()
        f.close()

        return str(data)

    def READ_AS_LIST(self):
        """
        returns data as a list
        :return:
        """
        f = open(self.data_file_name, 'r')
        data = f.readlines()
        f.close()

        return data
