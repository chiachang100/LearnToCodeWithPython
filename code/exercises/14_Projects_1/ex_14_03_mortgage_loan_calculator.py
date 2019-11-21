#!/usr/bin/python
# Filename: mortgage_loan_calculator.py

termsInYears = 30
interestRateYearly = 0.0375
loanAmount = 1000000

def getValues():
    global termsInYears
    global interestRateYearly
    global loanAmount

    try:
        termsInYears = int(input("Terms in Years (e.g. 30): "))
    except:
        pass

    try:
        interestRateYearly = float(input("Interest Rate (e.g. 0.0375): "))
    except:
        pass

    try:
        loanAmount = int(input("Loan Amount (e.g. 1000000): "))
    except:
        pass

def calculateMonthlyMortgagePayment(loanAmount, interestRateYearly, termsInYears):
    p = loanAmount
    i = interestRateYearly / 12
    n = termsInYears * 12
    m = p * (i * (1 + i) ** n)/((1 + i) ** n - 1)
    return m

#
if __name__ == "__main__":

    getValues()

    print()
    print("Mortgage Calculator\n")
    print("Terms in Years: {0}".format(termsInYears))
    print("Interest Rate (%): {0}".format(interestRateYearly*100))
    print("Loan Amount ($): {0}".format(loanAmount))
    print()
    monthlyPayment = calculateMonthlyMortgagePayment(loanAmount, interestRateYearly, termsInYears)
    print("Your monthly payment: {0:.2f}".format(monthlyPayment))
