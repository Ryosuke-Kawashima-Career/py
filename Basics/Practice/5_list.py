def solution():
    expenses = [2200, 2350, 2600, 2130, 2190]
    answer1 = expenses[1] - expenses[0]
    answer2 = sum(expenses[0: 3])
    answer3 = (2000 in expenses)
    expenses.append(1980)
    expenses[4-1] -= 200