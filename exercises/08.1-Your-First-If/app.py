total = int(input('How much money do you have in your pocket\n'))

# YOUR CODE HERE
print(total)
if total > 100:
    print("Give me your money!")
if total > 50 and total <= 100:
     print("Buy me some coffe you cheap!")
if total < 50:
     print("You are a poor guy, go away")
