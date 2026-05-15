import json

class ResultSaver:
        def __init__(self, data, output_path):
            self.data = data
            self.output_path = output_path

        def save(self):
            with open(self.output_path, 'w') as f:
                json.dump(self.data, f, indent=4)
            print(f"Результаты сохранены в {self.output_path}")