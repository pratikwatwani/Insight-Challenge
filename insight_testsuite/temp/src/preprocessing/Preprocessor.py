import datetime

class Preprocessor:
    def __init__(self,inputList):
        self.dic = {}
        self.list = inputList
        
    
    def parseDateTime(self):
        """
        This functions takes in the input data and matches date column to appropriate
        datetime format using the default python package:datetime, with multiple formats existing
        it uses try-except blocks
        :return: a list of format-correct datetime values
        """
        for item_index in range(len(self.list)):
            time =  self.list[item_index][4]

            try:
                self.list[item_index].append((datetime.datetime.strptime(time,'%x %H:%M')).strftime('%Y-%m-%d %H:%M:%S'))
            except:
                pass
            try:
                self.list[item_index].append((datetime.datetime.strptime(time,'%m/%d/%y %H:%M:%S %p')).strftime('%Y-%m-%d %H:%M:%S'))
            except:
                pass

        return self.list
    
    
