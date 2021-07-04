import os
import csv
poll_path = os.path.join('..','Resources', 'election_data.csv)
#open and read csv
with open(poll_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

#Variables
votes = []
candidates = []
counter = {"Khan": 0,"Correy": 0,"Li": 0,"O'Tooley": 0}

    for row in csvreader:

        votes.append(row)
        candidates.append(row[2])
#Election results

for candidate in candidates:
    if candidate == "Khan":
        counter["Khan"] += 1
    elif candidate == "Correy":
        counter["Correy"] += 1
    elif candidate == "Li":
        counter["Li"] += 1
    elif candidate == "O'Tooley":
        counter["O'Tooley"] += 1

    votes_for_khan = int(counter["Khan"])
    votes_for_correy = int(counter["Correy"])
    votes_for_li = int(counter["Li"])
    votes_for_otooley = int(counter["O'Tooley"])

    total = votes_for_khan + votes_for_correy + votes_for_li + votes_for_otooley
    khan = (votes_for_khan / votes) * 100
    correy = (votes_for_correy / votes) * 100
    li = (votes_for_li / votes) * 100
    otooley = (votes_for_otooley/votes) *100

print(f"Election Results")
print("--------------------")
print(f"Total Votes: {len(votes)}")
print("---------------------")
print(f"Khan: {round(khan)} ({counter['Khan']})")
print(f"Correy: {round(correy)} ({counter['Correy']})")
print(f"Li: {round(li)} ({counter['Li']})")
print(f"P'Tooley: {round(otooley)} ({counter['OTooley']})")
print("----------------------")
print(f"winner: Khan")
print("-----------------------")
