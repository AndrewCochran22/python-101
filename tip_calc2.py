bill_total = float(input("What is the total bill amount? "))
service = str(input("Was the service good, fair, or bad? "))
split = int(input("Split how many ways? "))

tip_amount = 0

if service == "good":
        tip_amount = .20 * bill_total
        print("Tip amount: $%.2f" % tip_amount)
        # print("Total amount: $%.2f" % total_amount)
elif service == "fair":
        tip_amount = .15 * bill_total
        print("Tip amount: $%.2f" % tip_amount)
        # print("Total amount: $%.2f" % total_amount)
elif service == "bad":
        tip_amount = .10 * bill_total
        print("Tip amount: $%.2f" % tip_amount)
        # print("Total amount: $%.2f" % total_amount)
else:
        print("Must be good, fair, or bad!")

total_amount = bill_total + tip_amount
print("Total amount: $%.2f" % total_amount)

per_person = total_amount / split
print("Amount per person: $%.2f" % per_person)