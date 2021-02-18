## This is a simple script that can calculate a few P/L metrics from a csv and write them to a .txt file


# Import Libraries
import pandas as pd 
from pathlib import Path

# Define path for csv and read to panda df
csv_path = Path("budget_data.csv")
budget_data = pd.read_csv(csv_path)

#Find the total number of months
def find_total_months(dataset):
    total_months = dataset.shape[0]
    return (f"Total Months: {total_months}")

#Find the net total amount of P/L over the entire period
def find_total_PL(dataset):
    total_PL = dataset["Profit/Losses"].sum()
    return (f"Total: ${total_PL}")


#Create new column with the change beteween all months

budget_data["change_from_prior_month"] = budget_data["Profit/Losses"].diff()

#Find average change

average_change_PL = round(budget_data.iloc[:,2].mean(), 2)


#Find Greatest Increase/decrease
max_idx = budget_data["change_from_prior_month"].idxmax()
min_idx = budget_data["change_from_prior_month"].idxmin()


file_path = Path("Financial_Analysis.txt")
with open(file_path, "w") as file:
    file.write("Financial Analysis \n")
    file.write("---------------------------- \n")
    file.write(str(find_total_months(budget_data)) + "\n")
    file.write(str(find_total_PL(budget_data)) + "\n")
    file.write(f"Average Change: ${average_change_PL} \n")
    file.write(f"Greatest Increase in Profits: {budget_data.iloc[max_idx, 0]} (${budget_data.iloc[max_idx, 2]}) \n")
    file.write(f"Greatest Increase in Profits: {budget_data.iloc[min_idx, 0]} (${budget_data.iloc[min_idx, 2]})")
with open(file_path, "r") as file:
    for line in file:
        print(line)
