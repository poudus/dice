import random
import sys

counter = []
for i in range(7):
	counter.append(0)

dices = []
nb = 3
if len(sys.argv) > 1:
	nb = int(sys.argv[1])

for i in range(nb):
	dices.append(random.randint(1,6))

print(dices)
print(sorted(dices))

for dice in dices:
	counter[dice] += 1

print(counter)
