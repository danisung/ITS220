scores = { }
result_f = open("results.txt")
for line in result_f:
	(name, score, age) = line.split()
	scores [score] = name + age
result_f.close()
print("The top scores were:")
for each_score in sorted(scores.keys(), reverse = True):
	print('Surfer ' + scores[each_score] + ' scored ' + each_score)	