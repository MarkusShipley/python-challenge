#######################################################################
############################# PART 1 - Import CSV FILE ################
#######################################################################

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

##########################################################################       
###########################Part 1 END - CSV FILE IMPORTED ################
##########################################################################


##########################################################################       
######## Part 2 - Import/Load CSV file data into Long_List ###############
##########################################################################

#Now that I can open and read the .csv file, the data needs to be saved into memory.
#Based on the structure of the data, I am going to create or have a nested list (list within a list) when the data is imported in
#Going to name my list long_list.  First, I must create an empty list before I can write the rows into it 
#Remember the = sign when declaring or setting a list.
#Note: Originally, I did not indent the long_list to be under the opening of the file.  Received I/O error on a closed file.

    long_list = []
    for row in csvreader:
        long_list.append(row)

#Had a print(long_list) but the final output was each row in tripilicate many 3 or 54 times.  So, I commented out and removed the print of the long_list until after the pop that removed the column headers
#The long list includes the header row.  I need to remove the header row so that I can do calculations on the remaining lists within the list.
#Lists are zero indexed and the header row will be included when the calculations are performed.  
#As a result, the pop() function is used because it allows index references to remove the column headers at the 0 index.
#Had to move the pop out of the iteration once I resolved the issue with the printing.
# QUESTION:WHy was the the multiple print(row) hosing up my output?  The strange this, the number of months counted correctly no matter how bizarre the print out was.
#Question: was it just the view of my data because of all of the prints but the nested table was actually ok?

    long_list.pop(0)
    print(long_list)

##########################################################################       
######## Part 3 - Total Number of Months in the data set #################
##########################################################################

#Now that the header has been removed using pop(), the length function can be used to get the number of months in the datase        
    number_of_months=len(long_list)
    print('number of months: ' + str(number_of_months))

#Total number of months or rows once the header is removed should be 86.  
#Number of months validates according to the results of the print statement

##########################################################################       
######## Part 4 - Total Profit and Loss over the entire period ###########
######## Also calculated the average PL for the full data set  ###########
######## Note: This average PL calced here is NOT the same as the ########
######## calc of the average change that occurs later.           #########
##########################################################################

#Assigning PL to long list and then printing values at index 1
    for PL in long_list:
        print(PL[1])

#Reviewed and confimred the print output

#Total PLs using Total_PL
#Initialize Total_PL and set it to 0 (zero)
# #Had to convert the PL values to int (integer) so that they could sum.  Without the int(PL[1]) line errored out
    Total_PL = 0
    for PL in long_list:
        Total_PL += int(PL[1])
    print('Total Profit and loss: ' + str(Total_PL))

    avg = Total_PL/number_of_months
    print('Average monthly Profile and Loss: ' + str(avg))
    
##########################################################################       
######## Part 5 - Total of the CHANGE in Profit and Loss       ###########
##########################################################################

#Calced the Total Profit and loss in Part 4. This section will focus on calculating the total of the CHANGES in PL
#Creating and empty set name 'nums' that will be populated with the monthly PL values at index 1. 
#These elements are converted to integer values so that in formulas and calculations may be performed on them
#Note to self: when creating a set or empty set, remember the =
    nums=[]
    for short_list in long_list:
        nums.append(int(short_list[1]))
    print(nums)

#Note: when 'nums' list was printed out, the values are in single quotes - meaning they are string and not integer.  
#Next code must convert the string data into integer like in initial solution above

#Create empty list to capture changes
#Create empty list to capture monthly variance.  Monthly variance will be appended with calculated monthly change
    monthly_changes = []
    monthly_variance = []

#Create a range start with 1 and going to length of nums.  Range will be used in a for loop
#we start with 1 instead of 0 because we are going to use a formula that subtracts i-1 the starting range number will get us to our first 0 index value
#Once monthly_changes are calculated, the monthly_variance list will be appended with the values calcualted
#An attempt was made to append monthly changes with the monthly changes, but the syntax failed.  This two step approach worked and the table values reconciled
    print(len(nums))
    for i in range(1, len(nums)):
        monthly_changes = (nums[i]-nums[(i-1)])
        monthly_variance.append(monthly_changes)
    print(monthly_variance)

#Output from monthly variance was printed to validate and confirm code and calculations

##########################################################################       
######## Part 6 - Mean (Average), Max and Min  ###########################
##########################################################################

#Calculation of Mean/Average
#Caclculated an average earlier.  However, the earlier calc was the average of each months PL. This section focuses on the mean, max and min of the varaince 
#Or delta/change from month to month
#Mean has to be imported into python

    from statistics import mean
    avg_variance = mean(monthly_variance)
    max_variance = max(monthly_variance)
    min_variance = min(monthly_variance)
    print('Average monthly PL Variance: ' + str(avg_variance))
    print('Max monthly PL Variance: ' + str(max_variance))
    print('Min monthly PL Variance: ' + str(min_variance))


##########################################################################       
######## Part 7 - Assigning a date to the Max and Min#####################
##########################################################################

#Earlier, the PL amounts were split from the dates and converted from int to string so that calcs could be performed
#At the start, we also removed the header column - which was located and index 0 - to get it out of the way so we had only the data with which to work
#Ventually, monthly variance list named monthly_variance was created that contained the difference in the PL for current and prior month
#With the header removed trom the original table, the index between the original table and monthly variance is one.
#If I insert zero or null into index position 0 of the monthly_variance list, the index for both tables will align
#once aligned, the index position of the varaince can determined and used in the retrieiving of the data from the first table

#insert None into monthly variance table at index 0 to align the index with the original table
    monthly_variance.insert(0,None)
    print(monthly_variance)

#Get index for Max and Min from the monthly variance table
    max_variance_index = monthly_variance.index(max_variance)
    min_variance_index = monthly_variance.index(min_variance)
    print(max_variance_index)
    print(min_variance_index)

#Split original long list into a short list of dates same as that in Step 2
    dates=[]
    for short_list_dates in long_list:
        dates.append(short_list_dates[0])
    print(dates)

#Get value from dates list using the max_varaince_index and min_variance_index values
#Note: This code commented out does not work.  However, the print statement using the results from earlier does work.  
#I can string the others together to get it to print.  However, not sure how to get it all into a file to save.
    #max_date_index=dates.index(max_variance_index)
    #min_date_index=dates.index(min_variance_index)
    #max_date_index=long_list.index(25)
    #min_date_index=long_list.index(44)
    print(dates[max_variance_index])
    print(dates[min_variance_index])

##########################################################################       
######## Part 8 - Terminal Print                     #####################
##########################################################################
    print('Financial Analysis')
    print('--------------------------------------')
    print('Number of Months: ' + str(number_of_months))
    print('Total Profit and loss: ' + str(Total_PL))
    print('Average monthly Profit and Loss: ' + str(avg))
    print('Average monthly PL Variance: ' + str(avg_variance))
    print('Max monthly PL Variance: ' + str(dates[max_variance_index]) + ': '+str(max_variance))
    print('Min monthly PL Variance: ' + str(dates[min_variance_index]) + ': '+str(min_variance))
    
##########################################################################       
######## Part 9 - Save file                          #####################
##########################################################################
    f = open('FinancialAnalysis.txt', 'w')
    f.write('Financial Analysis\n')
    f.write('--------------------------------------\n') #The new-line character has been used
    f.write('Number of Months: ' + str(number_of_months)+'\n')
    f.write('Total Profit and loss: ' + str(Total_PL)+'\n')
    f.write('Average monthly Profit and Loss: ' + str(avg)+'\n')
    f.write('Average monthly PL Variance: ' + str(avg_variance)+'\n')
    f.write('Max monthly PL Variance: '+ str(dates[max_variance_index]) + ': ' + str(max_variance)+'\n')
    f.write('Min monthly PL Variance: '+ str(dates[min_variance_index]) + ': ' + str(min_variance)+'\n')
    f.write('--------------------------------------\n')
    f.close()
f.close() #Closes the main file opened at start of program