import csv

employee_file = open('employee_data.csv', 'r')

csv_file = csv.reader(employee_file, delimiter=',')

next(csv_file)

for row in csv_file:

    employee_id = row[0]
    name = row[1]
    age = row[2]
    salary = float(row[3])
    hours_worked = row[4]
    productivity = row[5]
    team = row[6]
    bonus_rate = float(row[7])

    bonus = salary * bonus_rate
    total_pay = salary + bonus

    print(f"Employee ID: {employee_id}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Hours Worked: {hours_worked}")
    print(f"Productivity: {productivity}")
    print(f"Team: {team}")
    print(f"Salary: ${salary:,.2f}")
    print(f"Bonus: ${bonus:,.2f}")
    print(f"Total Pay: ${total_pay:,.2f}")

    print()
    input("Press Enter to continue...")

employee_file.close()