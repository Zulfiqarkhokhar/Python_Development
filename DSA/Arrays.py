expense = [2200,2350,2600,2130,2190] # jan - may

# 1. In Feb, how many dollars you spent extra compare to January?

extras = expense[1] - expense[0]

print(f"Extra spent in Feb: {extras}")

# 2. Find out your total expense in first quarter (first three months) of the year.

total = 0

for i in range(3):
    total = total+expense[i]

print(f"Total Expense of fisrt quater: {total}")
