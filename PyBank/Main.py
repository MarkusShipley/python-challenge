# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#Based on the location of the python main.py file and the Resources folder, no need existed for the .. or any other command to move up and down the folders
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    #Command below defiined 'row' that I am going to use and leverage later to append my long list--move the data from just being read and printed.
    #once loaded into a list or nested list, I can start doing calcs and using python to leverage the data.
    
    #Nested liste does not appear tpo create if the two lines below run
    #for row in csvreader:
        #print(row)

#Now that I can open and read the .csv file, the data needs to be saved into memory.
#Based on the structure of the data, I am going to create or have a nested list (list within a list) when the data is imported in
#Going to name my list long_list.  First, I must create an empty list before I can write the rows into it 
#Remember the = sign when declaring or setting a list.
#Note: Originally, I did not indent the long_list to be under the opening of the file.  Received I/O error on a closed file.
    long_list = []
    for row in csvreader:
        long_list.append(row)
        
#The long list includes the header row.  I need to remove the header row so that I can do calculations on the remaining lists within the list.
#Lists are zero indexed and the header row will be included when the calculations are performed.  
#As a result, the pop() function is used because it allows index references to remove the column headers at the 0 index.
    
    long_list.pop(0)
    print(long_list)
#Now that the header has been removed using pop(), the length function can be used to get the number of months in the dataset
        
    number_of_months=len(long_list)
    print('number of months ' + str(number_of_months))
