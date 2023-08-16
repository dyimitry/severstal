import os


class Dir:

    def __init__(self, name_dir):
        self.name_dir = name_dir
        self.spisok_files = []

    def read(self):
        names_files = os.listdir(self.name_dir)
        absolute_path_do_dir = os.path.abspath(self.name_dir)
        for file in names_files:
            absolute_path_do_file = os.path.join(absolute_path_do_dir, file)
            if os.path.isfile(absolute_path_do_file):
                self.spisok_files.append(absolute_path_do_file)
