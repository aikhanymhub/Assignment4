import csv

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.students = []

    def load(self):
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            self.students = list(csv.DictReader(file))
        print("Data loaded successfully.")

    def preview(self):
        print("First 5 students:", self.students[:5])