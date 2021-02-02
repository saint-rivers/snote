class Entry:
    def __init__(self, name, filepath, timestamp):
        self.name = name
        self.filepath = filepath
        self.timestamp = timestamp

    def show_info(self):
        print(f'Entry name: {self.name}')
        print(f'Filepath: {self.filepath}')
        print(f'Time created: {self.timestamp}')

    def read_stack(self):
        with open(self.filepath, 'r') as stack_file:
            for line in stack_file.readlines():
                print(line, end='')