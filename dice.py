import random
import sys

def search(text, nb):
	count = counter.count(nb)
	if count > 0:
		print(str(count)+' '+text)

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

search('Carre', 4)
search('Brelan', 3)
search('Paire', 2)
