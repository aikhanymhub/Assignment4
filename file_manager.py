import os

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def check_file(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Файл {self.file_path} не найден!")

    def create_output_folder(self):
        if not os.path.exists('output'):
            os.makedirs('output')