import csv
import os

#os.chdir('insight_testsuite/tests/test_1/output')

class OutputHandler:
    def __init__(self, outputFilePath):
        self.outputFilePath = outputFilePath
        
    def save_to_csv(self,header,output):
        with open(self.outputFilePath, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(output)
            
        path = os.getcwd()
        print(path)
        return 'Save success!'
