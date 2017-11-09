import random
import sys

# fonction inutile, en ligne 58 je teste directement if counter.count(nb) > 0
def search_same(text, nb):
	count = counter.count(nb)
	if count > 0:
		print(str(count)+' '+text)
		return True
	else:
		return False

# search run from start position
def search_run_from(start, length):
	for i in range(length):
		if sortedDices[start+i] != sortedDices[start]+i:
			return False
	return True

# search run from all valid start positions
def search_run(length, nb):
	nb_run = 0
	for i in range(nb-length+1):
		if search_run_from(i, length):
			nb_run += 1
	return nb_run

counter = []
for i in range(7):
	counter.append(0)

dices = []
nb_dices = 3
if len(sys.argv) > 1:
	nb_dices = int(sys.argv[1])

for i in range(nb_dices):
	dices.append(random.randint(1,6))

print(dices)
sortedDices = sorted(dices)
print(sortedDices)

for dice in dices:
	counter[dice] += 1

print(counter)

nb_run2 = search_run(2, nb_dices)
if (nb_run2 > 0):
	print(str(nb_run2)+' suites de longueur 2')

nb_run3 = search_run(3, nb_dices)
if (nb_run3 > 0):
	print(str(nb_run3)+' suites de longueur 3')

# example pour tester une paire et une serie de 3
if counter.count(2) > 0 and search_run(3, nb_dices) > 0:
	print('paire et serie de 3')
