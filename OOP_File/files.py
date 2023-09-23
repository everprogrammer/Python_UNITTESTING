import os

# Set current working direcory

class Files:

    def __init__(self, filename=None):
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.filename = None
        if filename:
            self.set_filename(filename)
        self.memory = None

    def set_filename(self, filename):
        self.filename = os.path.join(self.cwd, filename)

    def read_file(self):
        if self.filename:
            try:
                with open(self.filename, 'r') as file_to_read:
                    data = file_to_read.readlines()
                return data
            except FileNotFoundError as e:
                raise FileNotFoundError(f'{self.filename} does not exist!')
        else:
            raise ValueError('Filename is not set!')
    
    def write_file(self, content, mode):
        if self.filename:       
            with open(self.filename, mode) as file_to_write:
                file_to_write.writelines(str(content))
            return 'Writing done!'
        else:
            raise ValueError('Filename is not set!')

    def set_memory(self):
        self.memory = self.read_file()

    def get_memory(self):
        return self.memory

# f = Files('data.txt')
# data = f.read_file()
# print(data)
# ['Line 1 of test file!\n', 'Line 2 of test file!\n', 'Line 3 of test file!']