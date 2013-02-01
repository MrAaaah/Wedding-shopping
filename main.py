# -*-coding:Utf-8 -*
import itertools

# parsing du fichier (on colle tout dans des listes)
f = open('input.txt', 'r')

nbGarments = int(f.readline())

l = list()
money = list()
size = list()

for i in xrange(nbGarments):
	(m, nb) = f.readline().split()

	l.append(list())

	# on stock le nb d'argent
	money.append(int(m))
	size.append(int(nb))

	for j in xrange(int(nb)):
		models = f.readline().split()
		
		l[i].append(list())

		for k in xrange(int(models[0])):
			l[i][j].append(models[k + 1])


# recherche d'achat optimal via bruteforce (test de toutes les valeurs une par une)
for i in xrange(len(l)):
	combs = list(itertools.product(*l[i])) # toutes les combinaison possible pour la catégorie i
	maxCost = 0

	for comb in combs:
		cost = 0
		for elmt in comb:
			cost += int(elmt)

		if money[i] > cost > maxCost:
			maxCost = cost

	if maxCost == 0:
		print "No solution"
	else:
		print maxCost
