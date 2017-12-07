'''
	HW3 :  Compare the results between simulation and 
	       value calculated by long-term state formula

	Error Define :
	       (Formula value - Simulation value) / Formula value
'''
import simu_phase1 as sp1
import sys



def getNL (lo) :
	return (lo**2 / (1-lo))


def getNS (lo) :
	return (lo / (1-lo))


def getTL (lo, arrRate) :
	return ( lo**2 / ((1-lo) * arrRate) )


def getTS (lo, arrRate) :
	return ( lo / ((1-lo) * arrRate) )


def getERR (cor, sim) :
	return (cor-sim) / cor


if __name__ == "__main__" :

	sp1.checkArg ()
	sampleNum = int (sys.argv[1])
	arrRate = float (sys.argv[2])
	serRate = float (sys.argv[3])

	# Get Simulation Results from HW2
	arrivalT = sp1.getArrival (arrRate, sampleNum)
	serviceT = sp1.getService (serRate, sampleNum)
	quitQueueT = sp1.getQuitQueue (arrivalT, serviceT, sampleNum)
	leaveT = sp1.getLeave (serviceT, quitQueueT, sampleNum)
	avgP, avgQP, busy, idle = sp1.getSimuStat (arrivalT, leaveT, sampleNum)

	waitT = sp1.getWaiting (arrivalT, quitQueueT, sampleNum)
	waitTavg = sp1.stat.mean (waitT)
	staySysT = sp1.getStaySystem (arrivalT, leaveT, sampleNum)
	staySysTavg = sp1.stat.mean (staySysT)


	# Get Long-Term Results from formula
	lo = arrRate / serRate
	NS = getNS (lo)
	NL = getNL (lo)
	TS = getTS (lo, arrRate)
	TL = getTL (lo, arrRate)


	# Error Rate
	errUtil = getERR (lo, busy)
	errIdle = getERR ((1-lo), idle)
	errNS = getERR (NS, avgP)
	errNL = getERR (NL, avgQP)
	errTS = getERR (TS, staySysTavg)
	errTL = getERR (TL, waitTavg)


	print ("Simulation Results :")
	print ("--------------------")
	print ("Utilization rate of server                 :    ", busy*100, '%')
	print ("Average people in queue(line)         (nl) :    ", avgQP)
	print ("Average people in system              (ns) :    ", avgP)
	print ("Average waiting time in queue(line)   (tl) :    ", waitTavg)
	print ("Average time in system                (ts) :    ", staySysTavg)
	print ("Probability of no customers in system (P0) :    ", idle*100, '%')
	print ("\n===============================================================\n")
	print ("Formula Results :")
	print ("--------------------")
	print ("Utilization rate of server                 :    ", lo*100, '%')
	print ("Average people in queue(line)         (nl) :    ", NL)
	print ("Average people in system              (ns) :    ", NS)
	print ("Average waiting time in queue(line)   (tl) :    ", TL)
	print ("Average time in system                (ts) :    ", TS)
	print ("Probability of no customers in system (P0) :    ", (1-lo)*100, '%')
	print ("\n===============================================================\n")
	print ("Error Rate :")
	print ("--------------------")
	print ("Utilization rate of server                 :    ", errUtil)
	print ("Average people in queue(line)         (nl) :    ", errNL)
	print ("Average people in system              (ns) :    ", errNS)
	print ("Average waiting time in queue(line)   (tl) :    ", errTL)
	print ("Average time in system                (ts) :    ", errTS)
	print ("Probability of no customers in system (P0) :    ", errIdle, '\n')

