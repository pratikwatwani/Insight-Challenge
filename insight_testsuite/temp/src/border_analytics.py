from storage.InputHandler import InputHandler
from storage.OutputHandler import OutputHandler
from preprocessing.Preprocessor import Preprocessor
from computation.BorderCrossingComputation import BorderCrossingComputation
import argparse
import sys
import os


'''
Main file that is called with run.sh shell script,
this python file breaks down all computations in to 
several different small components.
'''
class BorderAnalytics:
    def __init__(self,inputFile,outputFilePath):
        self.input = inputFile
        self.outputFilePath = outputFilePath
        self.inputHandler = None
        self.outputHandler = None
        self.preprocessor = None
        self.borderCrossingCompute = None
        
    def inputFile(self,name):
        """
        This function fetches the input file from
        the name given and redirects it to the
        InputHandler.py file to get input data
        rows in a lists
        :param string name: name of the input file
        :returns: input file in list
        """
        self.inputHandler = InputHandler(name)
        return self.inputHandler.parse()
        
    def preprocess(self,inputList):
        """
        This function parses date time values into
        correct format.
        :param inputList: list of input data
        :return: parsed list of date time values
        """
        self.preprocessor = Preprocessor(inputList)
        return self.preprocessor.parseDateTime()
        
    def computeTotalCrossing(self):
        """
        This function computes the total crossing for each
        defined condition
        :return: a sorted array of data with total crossings value
        """
        store = self.inputFile(self.input)
        print("Store size:"+str(len(store)))
        
        processedList = self.preprocess(store)
        print("List processed:"+str(len(store)))
        
        self.borderCrossingCompute = BorderCrossingComputation(processedList)
        
        print("Starting computation for total crossing")
        self.borderCrossingCompute.computeTotalCross()
        print("Finished")
        
        return self.borderCrossingCompute.get_total_cross()
    
    def computeAverageCrossing(self):
        """
        This function computes the average for each category
        as required
        :return: a dictionary of computed averages
        """
        print("Starting avg cross computation")
        self.borderCrossingCompute.calculate_running_avg()
        print("Finished")
        
        return self.borderCrossingCompute.get_monthly_avg()
    
    def startAnalysis(self):
        """
        This function starts the core computation process of
        the project
        :return: a sorted list of final output
        """
        totalCrossing = self.computeTotalCrossing()
        avgCrossing= self.computeAverageCrossing()
        
        print("Merging results")
        output = self.borderCrossingCompute.getTotalCrossAndAverage()
        print("Finished")
        
        print("Saving output")
        self.saveOutput(output)
        
        
    def saveOutput(self,output):
        """
        This function saves the output list data structure
        into a csv file
        :param output: list of output rows
        """
        self.outputHandler = OutputHandler(self.outputFilePath)
        header = ["Border","Date","Measure","Value","Average"]
        status = self.outputHandler.save_to_csv(header,output)
        
        



parser = argparse.ArgumentParser()
parser.add_argument("inputFile", help="Input csv file for Analytics")
parser.add_argument("outputFilePath", help="dir for analytics output")

args = parser.parse_args()

analytics = BorderAnalytics(args.inputFile,args.outputFilePath)
analytics.startAnalysis()

    

