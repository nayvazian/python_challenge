import os
import csv

poll_csv = os.path.join("Resources", "election_data.csv")

#The total number of votes cast
with open(poll_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    header = next(csvreader)
    votenum = len(list(csvreader))
#The total number of votes each candidate won

otooley = 0
khan = 0
correy = 0
li = 0
with open(poll_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        if str(row[2]) == str("O'Tooley"):
            otooley += 1
        elif str(row[2]) == str("Khan"):
            khan+= 1
        elif str(row[2]) == str("Correy"):
            correy += 1
        elif str(row[2]) == str("Li"):
            li += 1

#The percentage of votes each candidate won
perc1 = otooley/votenum
perc2 = khan/votenum
perc3 = correy/votenum
perc4 = li/votenum



#The winner of the election based on popular vote.
Cands = {otooley:"O'Tooley", 
        khan:"Khan", 
        correy:"Correy", 
        li:"Li"}

winner = max(otooley, khan, correy, li)

print('Election Results')
print('----------------')
print(f'Total Votes: {votenum}')
print('----------------')
print(f"O'Tooley: {perc1} {otooley}")
print(f"Khan: {perc2} {khan}")
print(f"Correy: {perc3} {correy}")
print(f"Li: {perc4} {li}")
print('----------------')
print(f'Winner: {Cands.get(winner)}')
print('----------------')

#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------

