bill_total = float(input("What is the total bill amount? "))
service = str(input("Was the service good, fair, or bad? "))

tip_amount = service

if service == good:
    tip_amount == .20
elif service == fair:
        tip_amount == .18
elif service == bad:
        tip_amount == .15
else: print("Choices are good, fair, or bad.")

total = bill_total + tip_amount

