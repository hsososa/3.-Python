import os
import csv

budget_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

date = []
pro_loss = []
pro_loss_diff = []


with open(budget_csv) as csvfile:

    print("Finanacial Analysis")
    print('----------------------------')
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
        diff = pro_loss[i] - pro_loss[i - 1]
        pro_loss_diff.append(diff)

#    print(pro_loss_diff)

    def mean(numbers):           # This average function was taken from Python Day 3, Activity 7
        length = len(numbers)
        total = 0.0

        for number in numbers:
            total += number
        return total / length

    mean_diff = round(mean(pro_loss_diff),2)      # rounded to 2 decimals like in example analysis
    print(f'Average Change: ${mean_diff}')

    # Determining the greatest increase and decrease in profits over the entire period
    increase = max(pro_loss_diff)
    decrease = min(pro_loss_diff)
    # find the index (location) of the greatest increase and decrease
    increase_index = pro_loss_diff.index(increase)
    decrease_index = pro_loss_diff.index(decrease)
    # use the index to find the associated month of the greatest increase and decrease
    increase_month = date[increase_index + 1]
    decrease_month = date[decrease_index + 1]

    print(f"Greatest Increase in Profits:{increase_month} (${increase})")
    print(f"Greatest Decrease in Profits: {decrease_month} (${decrease})")

    # Outputting a text file with results of analysis
    os.chdir(r"C:\Users\nsososa1\Documents\GT Boot Camp\python-challenge\PyBank\Analysis")
    print(f"Total Months: {total_months}\n", file=open("bank_analysis.txt", "w"))
    print(f"Total: $ {net_total}\n", file=open("bank_analysis.txt", "a"))
    print(f"Average Change: $ {mean_diff}\n", file=open("bank_analysis.txt", "a"))
    print(f"Greatest Increase in Profits:{increase_month} (${increase})\n", file=open("bank_analysis.txt", "a"))
    print(f"Greatest Decrease in Profits: {decrease_month} (${decrease}\n", file=open("bank_analysis.txt", "a"))


