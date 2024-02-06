def print_bill(bill):
    total_bill = bill + bill * .15
    print(total_bill)

print_bill(600)
print_bill(500)

tax = .15
bill_for_diner_one = 600 + 600 * tax
print(bill_for_diner_one)
bill_for_diner_two = 500 + 500 * tax
print(bill_for_diner_two)