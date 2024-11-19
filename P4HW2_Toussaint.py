# Nexabet C. Tousssaint
# 11/18/2024
# P4HW2
# Program calculates paycheck based on over time or no over time

employee_name = input("Enter employee's name or Done to terminate: ")
Employees_entered = 0
Total_OT_Pay = 0
Total_RegPay = 0
Total_Gross = 0
# Input
while employee_name.lower() != "done":
    Employees_entered +=1
    hours = int(input(f"How many hours did {employee_name} work: "))
    pay_rate = float(input(f"What is {employee_name} pay rate?: "))
    if hours > 40:
        OT_hours = hours - 40
        reg_pay = pay_rate * 40
        OT_pay_rate =  pay_rate * 1.5
        OT_pay = OT_pay_rate * OT_hours
        Gross_pay = reg_pay + OT_pay

    else: 
        OT_hours = 0
        reg_pay = hours * pay_rate
        OT_pay_rate =  pay_rate * 1.5
        OT_pay = OT_pay_rate * OT_hours
        Gross_pay = reg_pay

    print("-" * 84)
    Total_OT_Pay = Total_OT_Pay + OT_pay
    Total_RegPay = Total_RegPay + reg_pay
    Total_Gross = Total_Gross + Gross_pay

    # Display result aka pay

    print(f"Employee name:    {employee_name}")
    print()
    print(f"{'Hours worked':<15}{'Pay rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross pay':<15}")
    print("-" * 84)
    print(f"{hours:<15}{pay_rate:<15.2f}{OT_hours:<15.2f}{OT_pay:<15.2f}${reg_pay:<15.2f}${Gross_pay:<15.2f}")

    employee_name = input("Enter employee's name or Done to terminate: ")
print()

# Display totals

print(f"Total number of employees entered: {Employees_entered}")
print(f"Total amount paid for overtime: ${Total_OT_Pay:.2f}")
print(f"Total amount paid for regular hours: ${Total_RegPay:.2f}")
print(f"Total amount paid in gross: ${Total_Gross:.2f}")





