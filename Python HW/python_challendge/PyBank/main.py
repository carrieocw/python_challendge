#make sure its working 
print("Hello")

#read in the csv file
import os
import csv

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')
file_to_output = os.path.join('Analysis','electionanalysis.txt')
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    previousrow = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # variables
    countmonths = 1
    nettotal = int(previousrow[1])
    changes = []
    greatestincrease = ['month',0]
    greatestdecrease = ['month',0]
    for row in csvreader:
        #print(row[1])
    #count the number of months in the dataset
        countmonths +=1
        nettotal +=int(row[1])
        change = int(row[1])-int(previousrow[1])
        previousrow = row
        changes.append(change)
        if change> greatestincrease[1]:
            greatestincrease[0]=row[0]
            greatestincrease[1]=change
        if change< greatestdecrease[1]:
            greatestdecrease[0]=row[0]
            greatestincrease[1]=change
    print(countmonths)
    print(nettotal)
    print(changes)
    print(greatestincrease)
    print(greatestdecrease)
# #The average of the changes in "Profit/Losses" over the entire period
    mean = sum(changes)/ len(changes)
    print(mean)
with open(file_to_output, 'w') as txtfile:
    txtfile.write(f"{candidates}:{vote_count}")

