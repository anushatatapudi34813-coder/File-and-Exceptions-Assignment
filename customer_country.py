import csv

customers = open('customers.csv', 'r')
outfile = open('customer_country.csv', 'w')

csv_file = csv.reader(customers, delimiter=',')

next(csv_file)

count = 0

for row in csv_file:
    full_name = row[1] + ' ' + row[2]
    country = row[4]

    outfile.write(full_name + ',' + country + '\n')

    count += 1

customers.close()
outfile.close()

print(f"Total customers read: {count}")