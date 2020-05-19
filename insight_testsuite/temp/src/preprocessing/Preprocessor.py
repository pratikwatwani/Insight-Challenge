import datetime

class Preprocessor:
    def __init__(self,inputList):
        self.dic = {}
        self.list = inputList
        
    
    def parseDateTime(self):
        for item_index in range(len(self.list)):
            time =  self.list[item_index][4]
            
            #print("T is  {}".format(time))
            try:
                #temp1 = (datetime.datetime.strptime(time,'%x %H:%M')).strftime('%Y-%m-%d %H:%M:%S')
                self.list[item_index].append((datetime.datetime.strptime(time,'%x %H:%M')).strftime('%Y-%m-%d %H:%M:%S'))
            except:
                pass
            try:
                #temp1 = (datetime.datetime.strptime(time,'%m/%d/%y %H:%M:%S %p')).strftime('%Y-%m-%d %H:%M:%S')
                self.list[item_index].append((datetime.datetime.strptime(time,'%m/%d/%y %H:%M:%S %p')).strftime('%Y-%m-%d %H:%M:%S'))
            except:
                pass

         
            
        return self.list
    
    
