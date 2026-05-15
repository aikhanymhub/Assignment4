class Report:
        def __init__(self, analyser, saver):
            self.analyser = analyser
            self.saver = saver

        def generate(self):
            print("Генерация отчета...")
            self.saver.save()