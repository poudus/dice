import random
import sys

# search run from start position
def search_run_from(start, length):
	for i in range(length):
		if counter[start+i] == 0:
			return False
	return True

# search run from all valid start positions
def search_run_counter(length):
	nb_run = 0
	for i in range(1, 6-length+2):
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

nb_run4 = search_run_counter(4)
if (nb_run4 > 0):
	print(str(nb_run4)+' suites de longueur 4')

nb_run3 = search_run_counter(3)
if (nb_run3 > 0):
	print(str(nb_run3)+' suites de longueur 3')
