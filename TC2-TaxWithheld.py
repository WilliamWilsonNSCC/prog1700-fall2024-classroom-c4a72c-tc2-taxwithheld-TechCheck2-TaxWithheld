# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

"""
Student Name: William Wilson
Program Title: Logic and Programming
Description: Tech Check 2
"""

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #collect input from user related to weekly salary
    weeklySalary=int(input("Please tell me how much you made this week: "))
    #collect input from user related to dependentsCollected
    dependentsCollected=int(input("Please input how many dependents you have: "))
    #depedents= dependentscollected * .02
    dependents= float(dependentsCollected * .02)
    #totalDependents= weeklySalary * dependents
    totalDependents= float(weeklySalary) * dependents

    #tax withheld from weekly salary
    #provincialTax= weeklySalary * .06
    provincialTax= weeklySalary *.06
    #federalTax= weeklySalary * .25
    federalTax= weeklySalary * .25
    #totalWithheld= provincialTax + federalTax - totalDependents
    totalWithheld= provincialTax + federalTax - totalDependents
    #totalTakeaway= totalwithheld-weeklysalary
    totalTakeaway= weeklySalary - totalWithheld

    print("Provincial Tax Withheld: ${0:.2f} \nFederal Tax Withheld: ${1:.2f} \nDependent Deducted from {2} dependents: ${3:.2f} \nTotal Withheld: ${4:.2f} \nTotal Pay Deposited: ${5:.2f}".format(provincialTax, federalTax, dependentsCollected, totalDependents, totalWithheld, totalTakeaway))
    # YOUR CODE ENDS HERE
    
main()
