import pickle
from datetime import datetime
count = 0

def hanoi(n, from_rod, to_rod, aux_rod):
	global count
	count = count + 1
	if n == 1:
		# print "Move disk 1 from rod", from_rod, "to rod", to_rod
		return
	hanoi(n-1, from_rod, aux_rod, to_rod)
	# print "Move disk", n, "from rod",from_rod, "to rod", to_rod
	hanoi(n-1, aux_rod, to_rod, from_rod)


trials = 35
steps = []
times = []
for i in range(1, trials + 1):
	count = 0
	startTime = datetime.now()
	hanoi(i, 'A', 'B', 'C')
	times.append((datetime.now() - startTime).total_seconds())
	steps.append(count)

with open("times.txt", "wb") as times_file:
	pickle.dump(times,times_file)

with open("steps.txt", "wb") as steps_file:
	pickle.dump(steps,steps_file)
