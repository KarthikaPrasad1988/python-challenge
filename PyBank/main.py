# main.py in PyBank
import os
import csv

# Path to the CSV file
csv_path = os.path.join("Resources", "budget_data.csv")

total_months = 0
net_total = 0
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}
previous_profit_loss = None

# Read the CSV file
with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#next header line
    next(csvreader)

    for row in csvreader:
        #data from the row
        date = row[0]
        profit_loss = int(row[1])
        
        #total months and net total
        total_months += 1
        net_total += profit_loss

        #change in profit/loss
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
 
            if change > greatest_increase["amount"]:
                greatest_increase ["date"] = date
                greatest_increase["amount"] = change

            if change < greatest_decrease["amount"]:
                greatest_decrease ["date"] = date
                greatest_decrease["amount"] = change


        previous_profit_loss = profit_loss

#print the results
print("Financial analysis")
print(".....................")
print(f"total months:{total_months}")
print(f"total: ${net_total}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']}")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} ($(greatest_decrease['amount'])")

#resuts in text file


output_path = os.path.join("Analysis", "financial_analysis.txt")
with open(output_path, "w") as output_file:
    output_file.write("financial analysis\n")
    output_file.write("--------------------\n")
    output_file.write(f"Total_months:{total_months}")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']}\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']}) (${greatest_decrease['amount']})")

print(f"Results written to {output_path}")
                                                                                                                                                                                                                                                                     



        


