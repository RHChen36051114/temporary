'''
	Simulate a M/M/1 queueing model
'''
import random as r
import sys
import math as m
import statistics as stat


# Generate Exponential Random Variable
def exporv (rate):
	return (-1/rate)*(m.log(r.random()))


# Check argument and print hint message
def checkArg () :
	if len(sys.argv) != 4 :
		print ("\n\tUsage  :    python  simu.py  [Simulate Amount]  [Arrival Rate]  [Service Rate]\n")
		sys.exit()



if __name__ == "__main__":

	checkArg()

	snum = int(sys.argv[1])

	arrivalT = []
	serviceT = []
	tmparr=0
	tmpser=0
	for cnt in range(snum):
		#tmparr += exporv(0.7)
		#tmpser = exporv(1.0)
		tmparr += exporv(float(sys.argv[2]))
		tmpser = exporv(float(sys.argv[3]))
		arrivalT.append(tmparr)
		serviceT.append(tmpser)


	# Initialization
	quitQueueT = [arrivalT[0]]
	arr = 0
	lev = 0
	sys = 0
	sysState = [0]
	total = 0
	queueP = 0
	tmpT = arrivalT[0]
	busy = 0


	# Maintain enter & quit queue time
	for cnt in range (1, snum) :
		if (arrivalT[cnt] - (quitQueueT[cnt-1] + serviceT[cnt-1])) >= 0 :
			quitQueueT.append (arrivalT[cnt])
		else :
			quitQueueT.append (quitQueueT[cnt-1] + serviceT[cnt-1])


	# Each customer waiting time
	waitT = []
	for cnt in range(snum) :
		if quitQueueT[cnt]-arrivalT[cnt] > 0 :
			waitT.append (quitQueueT[cnt] - arrivalT[cnt])
		else :
			waitT.append (0)

	# Each customer leaving system's time
	leaveT = []
	for cnt in range (snum) :
		leaveT.append (quitQueueT[cnt] + serviceT[cnt])


	# Each customer in system's time
	staySysT = []
	for cnt in range (snum) :
		staySysT.append (leaveT[cnt] - arrivalT[cnt])


	# Simulate system people condition
	#for cnt in range(len(arrivalT)+len(leaveT)-1) :
	while (arr+lev) < (len(arrivalT)+len(leaveT)-2) :
		m = min (arrivalT[arr], leaveT[lev])
		pos = [i for i,j in enumerate([arrivalT[arr], leaveT[lev]]) if j==m]
		
		if len(pos) == 1 and (arr != len(arrivalT)-1):
			# arrive
			if pos[0] == 0 :
				total += sys * (arrivalT[arr] - tmpT)

				# in queue
				if sys > 1 :
					queueP += (sys-1) * (arrivalT[arr] - tmpT)

				# record busy
				if sys > 0 :
					busy += arrivalT[arr] - tmpT

				tmpT = arrivalT[arr]
				sys += 1

				#sysState.append (sys)
				if arr < len(arrivalT)-1 :
					arr += 1

			# leave
			else :
				total += sys * (leaveT[lev] - tmpT)

				# in queue
				if sys > 1 :
					queueP += (sys-1) * (leaveT[lev] - tmpT)

				# record busy
				if sys > 0 :
					busy += leaveT[lev] - tmpT

				tmpT = leaveT[lev]
				sys -= 1

				#sysState.append (sys)
				if lev < len(leaveT)-1 :
					lev += 1

		else :
			# arrive = leave
			arr += 1
			lev += 1

	avgP = total / leaveT[snum-1]
	avgQP = queueP / leaveT[snum-1]
	busy = busy / leaveT[snum-1]
	idle = 1-busy

	print ("Utilization rate of server                 :    ", busy*100, '%')
	print ("Average people in queue(line)         (nl) :    ", avgQP)
	print ("Average people in system              (ns) :    ", avgP)
	print ("Average waiting time in queue(line)   (tl) :    ", stat.mean(waitT))
	print ("Average time in system                (ts) :    ", stat.mean(staySysT))
	print ("Probability of no customers in system (P0) :    ", idle*100, '%')

