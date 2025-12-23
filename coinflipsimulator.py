from random import randint
import matplotlib.pyplot as plt
n = int(input("Enter number of times you would like to flip the coin:"))
total = n
resultcount = {'Heads': 0, 'Tails':0}
while n>0:
    toss = randint(0,1)
    if toss == 0:
        resultcount['Heads'] += 1
    else:
        resultcount['Tails'] += 1
    n = n - 1

print("Number of Heads :", resultcount['Heads'])
print("Number of Tails :", resultcount['Tails'])
print("Probability for getting Heads", resultcount['Heads']/total)
print("Probability for getting Tails", resultcount['Tails']/total)


labels = ['Heads', 'Tails']
values = [resultcount['Heads'], resultcount['Tails']]

plt.bar(labels, values)
plt.xlabel("Outcome")
plt.ylabel("Count")
plt.title("Coin Flip Results")
plt.show()

