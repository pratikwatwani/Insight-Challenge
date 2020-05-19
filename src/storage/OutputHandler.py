import csv
import os

#os.chdir('insight_testsuite/tests/test_1/output')

class OutputHandler:
    def __init__(self, outputFilePath):
        self.outputFilePath = outputFilePath
        
    def save_to_csv(self,header,output):
        """
        This function writes the final computed data into a csv file
        using the default csv package in python
        :param header: explicitly defined header row for the csv file
        :param output: the list of rows that need to be written to csv file
        """
        with open(self.outputFilePath, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(output)
            
        path = os.getcwd()
        print(path)
        return 'Save success!'
