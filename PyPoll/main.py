import os
import csv

#path to the csv file
csv_path = os.path.join("PyPoll/Resources", "election_data.csv")
#csv_path = "election_data.csv"

total_number_votes = 0
candidate_list = {}
winner_candidate =  {"name": None, "votes": 0}

#read csv file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        ballet_id = row [0]
        county = row[1]
        candidate = row[2]

        # Count total votes
        total_number_votes += 1

        # Count votes for each candidate
        if candidate in candidate_list:
            candidate_list[candidate] += 1
        else: 
            candidate_list[candidate] = 1


        #winner information for the first candidate
            if winner_candidate["name"] is None:
                winner_candidate["name"] = candidate
                winner_candidate["votes"] = 1

            #percentage of votes
for candidate, votes in candidate_list.items():
    percentage = (votes / total_number_votes) * 100
    candidate_list[candidate] = {"votes" : votes, "percentage": percentage}

          #update the winner in the election
    if total_number_votes > winner_candidate["votes"]:
        winner_candidate["name"] = candidate
        winner_candidate["votes"] = total_number_votes

            #print the results
print("Election Results")
print(".................")
print(f"total_votes: {total_number_votes}")
print("..................................")
for candidate,data in candidate_list.items():
    print(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})")
print("-------------------------")
print(f"winner: {winner_candidate['name']}")
print(".......................")

#results to the text file
output_path = os.path.join("PyPoll/analysis", "election_results.txt")
with open(output_path, "w") as output_file:
    output_file.write("Election  Results\n")
    output_file.write(".....................")
    output_file.write(f"Total Votes: {total_number_votes}\n")
    output_file.write("................\n")
    for candidate, data in candidate_list.items():
        output_file.write(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})\n")
    output_file.write(".....................\n")
    output_file.write(f"winner: {winner_candidate['name']}\n")
    output_file.write("....................\n")

print(f"Results written to {output_path}")        


