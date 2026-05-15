class DataAnalyser:
    def __init__(self, data):
        self.data = data
        self.result = {}

    def analyse(self):
        pass

    def print_results(self):
        print(f"Results: {self.result}")

class SleepAnalyser(DataAnalyser): 
    def analyse(self):
        counts = {}
        for s in self.data:
            major = s.get('major', 'Unknown')
            counts[major] = counts.get(major, 0) + 1
        self.result = counts
        return self.result

class GpaAnalyser(DataAnalyser):
    def analyse(self):
        gpas = [float(s['GPA']) for s in self.data if s.get('GPA')]
        self.result = {"avg_gpa": sum(gpas)/len(gpas)} if gpas else {}