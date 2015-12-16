class CSVReader(object):
    def __init__(self, file_path=None, file_obj=None):
        self.file_path = file_path
        self.file_obj = file_obj
        self.file_data = ''
        self.__load_file()

    def __load_file(self):
        if not self.file_obj:
            with open(self.file_path, 'rb') as f:
                self.file_data = f.readlines()
        else:
            self.file_data = self.file_obj.readlines()

    def dataGenerator(self):
        for line in self.file_data:
            _out = line.split(',')
            yield _out

