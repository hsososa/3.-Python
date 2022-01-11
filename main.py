import os
import csv

budget_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

date = []
pro_loss = []
pro_loss_diff = []


with open(budget_csv) as csvfile:

    # Read in data in budget_data.csv with ',' delimiter
    bank_data = csv.reader(csvfile, delimiter=',')
    
    header = next(bank_data)

    for row in bank_data:
        date.append(row[0])
        pro_loss.append(row[1])

    # Finding the total number of months included in the dataset
    total_months = len(date)
    print(f"Total Months: {total_months}")

    # Finding the net total amount of "Profit/Losses" over the entire period
    pro_loss = [int (profloss_values) for profloss_values in pro_loss]
    net_total = sum(pro_loss)
    print(f"Total: $ {net_total}")

    for i in range(1,len(pro_loss)):
        pro_loss_diff = pro_loss[i] - pro_loss[i - 1]
        diff_sum = pro_loss 
    mean_diff = sum(pro_loss_diff)/len(pro_loss_diff)
    
    # Outputting a text file with results of analysis
    os.chdir(r"C:\Users\nsososa1\Documents\GT Boot Camp\python-challenge\PyBank\Analysis")
    print(f"Total Months: {total_months}\n", file=open("bank_analysis.txt", "w"))
    print(f"Total: $ {net_total}\n", file=open("bank_analysis.txt", "a"))
#    print(f"Average Change: $ {mean_diff}\n", file=open("bank_analysis.txt", "a"))
#    print(f"Greatest Increase in Profits:\n", file=open("bank_analysis.txt", "a"))
#    print(f"Greatest Decrease in Profits:\n", file=open("bank_analysis.txt", "a"))


