import datetime

class BorderCrossingComputation:
    def __init__(self,inputList):
        self.dic = {}
        self.list = inputList
        self.totalCross = []

    def gen_key(self,border,means):
        """
        Utility function 1:
        This function is used to combine columns to treat them as one key
        for easier computation
        :param str border: value in each row of border
        :param str means: value in each row of means/measure
        :return: a string of combination of border and means separated by #
        """
        return border+"#"+means

    def gen_key2(self,border,date,means):
        """
        Utility function 2:
        This function is used to combine columns to treat them as one key
        for easier computation
        :param str border: value in each row of border
        :param datetime date: value in each row of date
        :param str means: value in each row of means/measure
        :return: a string of combination of border, means and date each separated by #
        """
        return border+"#"+date+"#"+means
    

    def computeTotalCross(self):
        """
        This function computes total cross that occurs at each border for all measure types
        :return: dictionary to hold the counts of entity based on Key(Border,Date,Measure) and value(count)
        """
        for index in range(len(self.list)):
            key = tuple(self.list[index][3:6])
            value = int(self.list[index][6])
            
            if key in self.dic:
                self.dic[key] += value
            else:
                self.dic[key] = value
                
        self.totalCross = self.transformResults()

        
    
    def get_total_cross(self):
        """
        This function returns totalCross from computeTotalCross()
        :return: a dictionary of total crossing counts based on Border, Date, Measure
        """
        return self.totalCross
    
    def transformResults(self):
        """
        This function transforms the results into a sorted list
        :return: a sorted list of items [Border,date,Measure,count]
        """
        arr = []
        
        for i in self.dic.keys():
            temp = list(i)
            temp.append(self.dic[i])
            arr.append(temp)
            
        return self.sortResults(arr)
    
    def sortResults(self,listArray):
        """
        Sorts the results of the input list into another list
        :param listArray:
        :return: sorted list
        """
        newArray = sorted(listArray, key=lambda x: (x[1], x[3], x[2], x[0]))
        newArray.reverse()
        return newArray
    
    
    #Time complexity is O(n)+O(time_required_to_sort) , assuming saving and retrival cost of dic is constant
    def calculate_running_avg(self,border_index=0,date_index=1,means_index=2,value_index=3):
        """
        Calculate the running average for each key, condition
        :param int border_index: index value to access border data item at
        :param int date_index: index value to access date data item at
        :param int means_index: index value to access measure/means data item at
        :param int value_index: index value to access value/sum data item at
        :return: a dictionary of computed rows of running average
        """
        run_avg = {}
        return_avg = {}
        td = []
        #For simplicity lets sort the dic in ascending order of date
        try:
            td = sorted(self.get_total_cross(), key=lambda x: datetime.datetime.strptime(x[date_index], '%m/%d/%Y %H:%M:%S %p'))

        except:
            pass
        try:
            td = sorted(self.get_total_cross(), key=lambda x: datetime.datetime.strptime(x[date_index], '%x %H:%M'))

        except:
            pass

        for item in td:
            key = self.gen_key(item[border_index],item[means_index])
            key2 = self.gen_key2(item[border_index],item[date_index],item[means_index])

            if(key in run_avg):
                value = run_avg[key]

                return_avg[key2] = value[0]/value[1]

                value[0]+=float(item[value_index])
                value[1]+=1
                run_avg[key] = value


            else:
                return_avg[key2] = 0
                value = [float(item[value_index]),1]
                run_avg[key] = value
        
        self.avg_monthly_run = return_avg
    
    def get_monthly_avg(self):
        """
        Get the monthly running average
        :return: returns avg_monthly run from calculate_running_average
        """
        return self.avg_monthly_run
    
    def getTotalCrossAndAverage(self):
        """
        Combines the results of total counts and running average into one list row
        :return: a list of final output [Border, Date, Measure, Value, Avg]
        """
        output = []

        for i in self.totalCross:
            temp = list(i)
        
            key = self.gen_key2(temp[0],temp[1],temp[2])
            temp.append(int(round(self.avg_monthly_run[key])))
            
            output.append(temp)
            
        return output
