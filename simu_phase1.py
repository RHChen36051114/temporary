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



def getArrival (rate, length) :
	arr = []
	tmp = 0
	for cnt in range(length) :
		tmp += exporv (float(rate))
		arr.append (tmp)
	return arr



def getService (rate, length) :
	return [exporv(float(rate)) for x in range(length)]



def getQuitQueue (arr, ser, length) :
	quit = [arr[0]]
	for cnt in range(1, length) :
		if (arr[cnt] - (quit[cnt-1]+ser[cnt-1])) >= 0 :
			quit.append (arr[cnt])
		else :
			quit.append (quit[cnt-1]+ser[cnt-1])
	return quit



def getWaiting (arr, quit, length) :
	return [(quit[x]-arr[x]) for x in range(length)]



def getLeave (ser, quit, length) :
	return [(quit[x]+ser[x]) for x in range(length)]



def getStaySystem (arr, leave, length) :
	return [(leave[x]-arr[x]) for x in range(length)]



def getSimuStat (arrivalT, leaveT, length) :
	arr = 0
	lev = 0
	sys = 0
	sysState = [0]
	total = 0
	queueP = 0
	tmpT = arrivalT[0]
	busy = 0

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

	avgP = total / leaveT[length-1]
	avgQP = queueP / leaveT[length-1]
	busy = busy / leaveT[length-1]
	idle = 1-busy

	return [avgP, avgQP, busy, idle]



def main(argv) :

	checkArg()

	snum = int(argv[1])
	arrivalT = getArrival (argv[2], snum)
	serviceT = getService (argv[3], snum)

	# Maintain enter & quit queue time
	quitQueueT = getQuitQueue (arrivalT, serviceT, snum)

	# Each customer waiting time
	waitT = getWaiting (arrivalT, quitQueueT, snum)

	# Each customer leaving system's time
	leaveT = getLeave (serviceT, quitQueueT, snum)

	# Each customer in system's time
	staySysT = getStaySystem (arrivalT, leaveT, snum)

	# Simulate system people condition
	avgP, avgQP, busy, idle = getSimuStat (arrivalT, leaveT, snum)

	print ("Utilization rate of server                 :    ", busy*100, '%')
	print ("Average people in queue(line)         (nl) :    ", avgQP)
	print ("Average people in system              (ns) :    ", avgP)
	print ("Average waiting time in queue(line)   (tl) :    ", stat.mean(waitT))
	print ("Average time in system                (ts) :    ", stat.mean(staySysT))
	print ("Probability of no customers in system (P0) :    ", idle*100, '%')



if __name__ == "__main__":
	main(sys.argv)

