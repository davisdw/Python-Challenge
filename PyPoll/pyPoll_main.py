import csv
import pandas as pd

file_pd_poll =  pd.read_csv('/Users/ddavis85/Python-Challenge/PyPoll/Resources/election_data.csv')

total_ballot = len(file_pd_poll)

candidate_ballot_count = file_pd_poll["Candidate"].value_counts()
   
percent_ballot_count = (candidate_ballot_count / total_ballot) * 100

candidate_winner = candidate_ballot_count.idxmax()

print("Here is the election Results:    ")
print(" ")
print("---------------------------------")
print(" ")
print("Total Votes:   " + str(total_ballot))
print(" ")
print("Charles Casper Stockham:   " + "%" + str(round(percent_ballot_count[1], 3)) + " " + "(" + str(candidate_ballot_count[1])+")")
print(" ")
print("Diana DeGette:   " + "%" + str(round(percent_ballot_count[0], 3)) + " " + "(" + str(candidate_ballot_count[0])+")")
print(" ")
print("Raymon Anthony Doane:   "+ "%" + str(round(percent_ballot_count[2], 3)) + " " + "(" + str(candidate_ballot_count[2])+")")
print(" ")
print(" ")
print("Winner:  " + candidate_winner)

output_result = open("pyPoll_output.txt", "w")

output_result.write("Here is the election Results:  ")
output_result.write("\n")
output_result.write("--------------------------------------------")
output_result.write("\n")
output_result.write("Total Votes:               " + str(total_ballot))
output_result.write("\n")
output_result.write("Charles Casper Stockham:   " + "%" + str(round(percent_ballot_count[1], 3)) + " " + "(" + str(candidate_ballot_count[1])+")")
output_result.write("\n")
output_result.write("Diana DeGette:             " + "%" + str(round(percent_ballot_count[0], 3)) + " " + "(" + str(candidate_ballot_count[0])+")")
output_result.write("\n")
output_result.write("Raymon Anthony Doane:      " + "%" + str(round(percent_ballot_count[2], 3)) + " " + "(" + str(candidate_ballot_count[2])+")")
output_result.write("\n")
output_result.write("Winner:  " + candidate_winner)

output_result.close()
