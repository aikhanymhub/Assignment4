from analytics.file_manager import FileManager
from analytics.data_loader import DataLoader
from analytics.result_saver import ResultSaver
from analytics.report import Report
from analytics.analyser import SleepAnalyser, GpaAnalyser

def main():
    file_manager = FileManager('students.csv')

    try:
        file_manager.check_file()
        file_manager.create_output_folder()
    except FileNotFoundError as error:
        print(error)
        return

    loader = DataLoader('students.csv')
    loader.load()
    loader.preview()

    print("\n------------------------------")
    print("Running all analysers:")
    print("------------------------------")

    analysers = [
        SleepAnalyser(loader.students),
        GpaAnalyser(loader.students[:10])
    ]

    for analyser in analysers:
        print(analyser)
        analyser.analyse()
        analyser.print_results()

    main_analyser = SleepAnalyser(loader.students)
    main_analyser.analyse()

    saver = ResultSaver(
        main_analyser.result,
        'output/result.json'
    )

    report = Report(main_analyser, saver)
    report.generate()

if __name__ == '__main__':
    main()