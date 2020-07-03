#make sure its working 
print("Hello")

#read in the csv file
import os
import csv

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')
file_to_output = os.path.join('Analysis','electionanalysis.txt')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

# Read the header row first 
    csv_header = next(csvreader)
    previousrow = next(csvreader)
    print(f"CSV Header: {csv_header}")
#createvariables 
    totalvotes = 0
    candidates ={}
  
#Count the total number of rows for total votes
    for row in csvreader:
        totalvotes +=1
        name=row[2]
        if name not in candidates:
           candidates[name]=1
        else:
            candidates[name]=candidates[name]+1

    print(totalvotes)
    for candidates, vote_count in candidates.items():
        print(f"{candidates}:{vote_count}")

with open(file_to_output, 'w') as txtfile:
    txtfile.write(f"{candidates}:{vote_count}")
# calculate the percentages






