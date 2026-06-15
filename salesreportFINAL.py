import csv

sales_file = open('sales.csv', 'r')
outfile = open('salesreportFINAL.csv', 'w')

csv_file = csv.reader(sales_file, delimiter=',')

next(csv_file)

customer_totals = {}

for row in csv_file:

    customer_id = row[0]

    subtotal = float(row[3])
    tax = float(row[4])
    freight = float(row[5])

    total = subtotal + tax + freight

    if customer_id in customer_totals:
        customer_totals[customer_id] += total
    else:
        customer_totals[customer_id] = total

outfile.write("Customer ID,Total\n")

for customer_id in customer_totals:
    outfile.write(f"{customer_id},{customer_totals[customer_id]:.2f}\n")

sales_file.close()
outfile.close()

print("salesreportFINAL.csv created successfully!")