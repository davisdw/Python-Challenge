import csv # reading csv file

#specified exact location of file path and opens the file
opencsv = open('/Users/ddavis85/Python-Challenge/PyBank/Resources/budget_data.csv')
csvreader = csv.reader(opencsv, delimiter=",")  # reads the content of that file
csv_header = next(csvreader) # skips the header


'''
Calculate the following: 
	
    Total number of months included
	
	Net total of amount of “Profit/Loss” over entire period 

	The Changes in “Profit/Loss” “-“ and then average of those changes

	The Greatest Increase  in profits (including date and amount) over entire period
	
	The Greatest decrease in profits (including date and amount) over entire period
'''

total_months = 0
net_total = 0
net_positive_change = 0
net_negative_change = 0


#previous_profit_change = 0

#using both variables to add the values profits and dates into the array list

dates = []
profits = []
for rows in csvreader:
    profits.append(int(rows[1]))
    dates.append(rows[0])
    total_months += 1
    net_total += int(rows[1])

    
    
# creating variable to store the length of the profits changes calculate the differences of the profits and gather the average

net_profit_change = []
for y in range(1, len(profits)):
        net_profit_change.append((int(profits[y] - int(profits[y-1]))))
   

average_profit_change = sum(net_profit_change) / len(net_profit_change)

#using min and max to determine the highest and lowest profit from the net_profit_change
greatest_increase_profit = max(net_profit_change)
least_increase_profit = min(net_profit_change)

# assigned these variable to determine the date that corresponds to the min and max profits
#invoked the index to locate the date that refereces to the min and max profits 
date_greatest_profit = dates[net_profit_change.index(max(net_profit_change))+1]
date_least_profit = dates[net_profit_change.index(min(net_profit_change))+1]

#format the numbers
currency_total = "{:,}".format(net_total)
currency_change = "{:.2f}".format(average_profit_change)
currency_greatest = "{:,}".format(greatest_increase_profit)
currency_least = "{:,}".format(least_increase_profit)



#Displaying output on the terminal results

print("Financial Analysis")
print(" ")
print("--------------------------------------------------")
print(" ")
print("Total Months:    " + str(total_months))
print(" ")
print("Total Profits:   " + "$",  currency_total)
print(" ")
print("Average Change in Profits:  " + "$", currency_change)
print(" ")
print("Greatest Increase in Profits:  " + str(date_greatest_profit) + " " + "$", currency_greatest)
print(" ")
print("Greatest Decrease in Profits:    " + str(date_least_profit) + " " + "S", currency_least)


#Print by exporting output in file

file_output = open("pyBank_output.txt", "w")

file_output.write("Financial Analysis")
file_output.write("\n")
file_output.write("--------------------------------------------------")
file_output.write("\n")
file_output.write("Total Months:    " + str(total_months))
file_output.write("\n")
file_output.write("Total Profits:  " + str(format(currency_total)))
file_output.write("\n")
file_output.write("Average Change in Profits: " + str(format(currency_change)))
file_output.write("\n")
file_output.write("Greatest Increase in Profits:  " + str(date_greatest_profit) + str(format(currency_greatest)))
file_output.write("\n")
file_output.write("Greatest Decrease in Profits:    " + str(date_least_profit) + str(format(currency_least)))



file_output.close()
