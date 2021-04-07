import os
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")
total = 0
with open(bank_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csvreader)

    #The net total amount of "Profit/Losses" over the entire period and the total number of months included in the dataset 
    x = next(csvreader)
    total += int(x[1])
    months = 1
    for row in csvreader:
        total += int(row[1])
        months = months + 1
    
    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    ave = total / months
    

#The greatest increase in profits (date and amount) over the entire period
with open(bank_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    header = next(csvreader)
    maxnum = max(csvreader, key=lambda row: int(row[1]))
    

#The greatest decrease in losses (date and amount) over the entire period
with open(bank_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    header = next(csvreader)
    minnum = min(csvreader, key=lambda row: int(row[1]))

print("Financial Analysis")
print("------------------")
print(f'Total months: {months}')
print(f'Total: {total}')
print(f'Average Change: {ave}')
print(f'Greatest Profit {maxnum}')
print(f'Greatest Loss {minnum}')
