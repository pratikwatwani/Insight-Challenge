# Border Crossing Analysis
## Insight Data Science challenge problem
https://github.com/InsightDataScience/border-crossing-analysis

## Libraries used
I've used all native packages/modules available in python by default, so no additional installation/pip is required.

1. os
2. csv
3. argparse
4. datetime

## Code
I've applied the OOP Concepts so it stands with respect to the industry standard, not only it is helpful in understanding the code but it also helps in easier debugging and transitions

As mentioned above, no other package is used in this project. 

There is one main python file border_analytics.py that will invoke necessary modules/functions and other python files for respective computations. 

I've broken down the entire process into smaller modules with each module serving as the name suggests, viz. 
1. Input - receiving input and transforming into respective data structure, 
2. Parsing Dates - parsing dates into appropriate date formats for easier computation, 
3. Computing Total Crossings - computing total crossings for each border, date and measure, 
4. Computing Average Crossings - computing running average for each border, date, measure and value, 
5. Merging the results - merging both total crossings and average crossings, 
6. Output - writing the merged results to csv

## Steps to run code:
`python src/border_analytics.py input/Border_Crossing_Entry_Data.csv output/report.csv`
