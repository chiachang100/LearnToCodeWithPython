#!/usr/bin/python
# Filename: compound_interest.py

principle = 10000
interestRates = [0.05, 0.06, 0.10, 0.11, 0.15, 0.20]
numberOfTimesCompounded = 1
numberOfYears = 5
maxiumOfYears = 40

def calculateCompoundInterest(principle, interestRate, numberOfTimesCompounded, numberOfYears):
    finalAmount = principle * ((1 + interestRate/numberOfTimesCompounded) ** numberOfYears)
    return finalAmount

#
print()
print("Compound Interest Calculator")
print("Initial Investment = $10,000")
print("Time\t\tRate Of Growth")
print("Years\t5%\t6%\t10%\t11%\t15%\t20%")
print("-"*60)
while (numberOfYears <= maxiumOfYears):
    print("{0}\t".format(numberOfYears), end="")
    for interestRate in interestRates:
        finalAmount = calculateCompoundInterest(principle, interestRate, numberOfTimesCompounded, numberOfYears)
        print("{0:.0f}".format(finalAmount), end="\t")
    print()
    numberOfYears += 5

