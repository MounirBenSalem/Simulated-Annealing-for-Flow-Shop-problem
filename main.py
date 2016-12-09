from fun import *
import time 

# start time

# Reading data from file 
while True :
    try:
        instanceName = raw_input(" instance name is = ")
        instanceFile = open(instanceName,'r')
        break
    except ( IOError, ValueError):
        print " Oops the instance name is false, remember to add .txt ... "
# create a matrix of processing time from the instance 
pt =  [ map(int,line.split()) for line in instanceFile ]
instanceFile.close()
m = len(pt)     # number of jobs
n = len(pt[0])  # number of machines
print "n =",n ,",  m =",  m 
while True :  # we are going to save the best solution in this file 
    try :
        resultName = "result_" + instanceName 
        resultSave = open(resultName,'w')
        break
    except ( IOError, ValueError):
        print "an error accured suddenly :O !! "

pt = np.array(pt)
print "processing time "
print pt

start_time = time.time()
seqOpt , miniMakeSpan = simAnneal ( n, m, pt )
print("\n --- %s seconds ---" % (time.time() - start_time))

print "la sequence optimale : ",seqOpt ,"\n Cmax =", miniMakeSpan

saveData = saveDat(seqOpt , miniMakeSpan , resultSave )
resultSave.close()


