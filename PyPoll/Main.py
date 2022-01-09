#######################################################################
############################# Step 1 - Import CSV FILE ################
#######################################################################

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#Based on the location of the python main.py file and the Resources folder, no need existed for the .. or any other command to move up and down the folders
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    


##########################################################################       
######## Step 2 - Import/Load CSV file data into votes list ##############
##########################################################################

#Now that the .csv file can be opened and read, the data needs to be saved into memory.
#Based on the structure of the data, I am going to create or have a nested list (list within a list) when the data is imported in
#Going to name the list votes. 

    votes = []
    for row in csvreader:
        votes.append(row)

#The votes list includes a header row.  The header row is being removed to make it easier to work with list.
#The pop() function is used because it allows index references to remove the column headers at the 0 index.

    votes.pop(0)
#Data set is very large -- do NOT do multiple prints throughout to confirm the data

##########################################################################  
#################### Step 3 (Question 1 - total votes)####################
##########################################################################  

#Now that the header row has been removed, we can use the length of the list to get the total voter count
    total_votes = len(votes)
    print('Total votes cast: ' +str(total_votes))

##########################################################################  
#################### Step 4 (Question 2 - Unique Candidates)##############
########################################################################## 

#Create an empty set called all names.  All names will be used to create a list of just the names from the votes list impoorted in step 1 and step 2
    all_names = []

    for vote in votes:
        name = vote[2]
        all_names.append(name)
#We did not cover the functionality below in class or in our exercises.  
#The line below should create a list called unique_names. The set command will convert the all names list to a set -- sets contain only unique values and should remove the duplicates.
#The list command in front of set should convert the set of unique values back to a list!
    unique_names = list(set(all_names))

    print(unique_names)

#Resulting output is ['Li', 'Correy', 'Khan', "O'Tooley"] = unique list of candidates

##########################################################################  
#################### Step 5 (Question 3 - Total Votes by Candidate)#######
########################################################################## 

#To determine the total votes by candidate, we are going to use a dictionary.  
#First, an empty dictionary named cand_votes will be created to "count the votes"
#Dictionaries have a key and a value.
#Next, a for loop will be utilized similar to that used in step 4. 
#An if statement will be used similary to step 4, that will update the value for key each time the key is encountered in the data file.
#If the name of the candidate isn't in the dictionary, it will add it with an initial value of 1
#If the name of the candidate is already a key in the dictionary, it will increate the value associated with the key by 1

    cand_votes = {}

    for vote in votes:
        name = vote[2]
        if name not in cand_votes.keys():
            cand_votes[name] = 1
        else:
            cand_votes[name] += 1

    print(cand_votes)

   
   
##########################################################################  
#################### Step 6 (Question 4 - % by Candidate)#################
########################################################################## 

#Using a dictionary to calculate the % by Candidate 
#Going to use the copy() dictionary function to to cpy the cand_votes dictionary to cand_pct dictionary to keep percent separate
    
    cand_pct = cand_votes
    for name, count in cand_pct.items():
        cand_pct[name] = count / total_votes * 100
    
    print(cand_pct)


    cand_votes = {}

    for vote in votes:
        name = vote[2]
        if name not in cand_votes.keys():
            cand_votes[name] = 1
        else:
            cand_votes[name] += 1

    print(cand_votes)
##########################################################################  
####################Step 7 (Question 5 - Elections winner)####################
#Either the cand_votes or cand_pst disctionary can be used
#Going to use max function that I read about that can be used with dictionaries
# https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python and https://pythonguides.com/python-find-max-value-in-a-dictionary/
##########################################################################  
    winner = max(cand_votes, key=cand_votes.get)

    print(winner)

##########################################################################  
####################Step 8  Generate File ################################
##########################################################################  
    f = open("electionanalysis.txt","w")
    f.write("Election Results\n")
    f.write("----------------------------------------------\n")
    f.write("Percent of Vote Received by Candidate\n")
    for name, value in cand_pct.items():
        f.write('%s:%s\n' % (name, value))
    f.write("----------------------------------------------\n")
    f.write("Election Winner: " + (winner) + '\n')
    f.write("----------------------------------------------\n")
    f.write('Total votes cast: ' + str(total_votes)+ '\n')
    f.close()

 ##########################################################################  
####################Step 8  Generate View to Terminal######################
########################################################################## 
    print("---------------------------------------------------")
    print('Total votes cast: ' +str(total_votes))
    print("---------------------------------------------------")
    print('Percentage votes received by candidate:')
    for name, value in cand_pct.items():
        print(name, value)
    print("---------------------------------------------------")
    print("Election Winner: " + (winner))
    print("---------------------------------------------------")