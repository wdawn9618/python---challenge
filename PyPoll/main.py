import os
import csv

poll_path = os.path.join('election_data.csv')
poll_path_out= os.path.join('election_date.txt')

#Variables
votes = 0
candidates = []
candid_votes = {}
winner =""
win_count = 0

with open(poll_path, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)

#Election Results
    for row in reader:
        print(". ", end=""),
        votes = votes + 1
        win_cand = row[2]

        if win_cand not in candidates:
            candidates.append(win_cand)
            candid_votes[win_cand] = 0

        candid_votes[win_cand] = candid_votes[win_cand] + 1

election_results =(
    f"\n\nElection Results\n"
    f"--------------------\n"
    f"Total Votes: {votes}\n"
    f"---------------------\n")
print(election_results, end="")

#Determine winner
for candidate in candid_votes:
        all_votes = candid_votes.get(candidate)
        vote_pctg = float(all_votes) / float(votes) * 100

        if(votes > win_count) :
            win_count = votes
            winner = candidate

output = f"{candidate}: {vote_pctg:.3f}% ({votes})\n"
print(output, end="")

final = (
    f"----------------------\n"
    f"Winner: {winner}\n"
    f"-----------------------\n")
print(final)


