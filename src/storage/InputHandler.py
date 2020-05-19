import csv

class InputHandler:
    def __init__(self, inputFileName):
        self.inputFile = inputFileName
        self.store = []
        
    
    def parse(self):
        """
        This function parses the input data from
        csv to a list of items
        :return: list of data
        """
        with open(self.inputFile, 'r') as f:
            reader = csv.reader(f)
            
            next(reader)
            for row in reader:
                self.store.append(row)

        return self.store