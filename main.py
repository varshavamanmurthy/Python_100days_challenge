print("Welcome to the tip Calculator.")
bill_total = float(input("What was the total bill?"))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12 or 15?'))
split = int(input("How many people to split the bill?"))

total_tips_given = bill_total * (tip_percentage / 100)
final = round((bill_total + total_tips_given) / split, 2)
print(f"Each person should pay : ${final}")

