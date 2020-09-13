import numpy as np
import csv
import sys
reader=csv.reader(open(sys.argv[1], "rU"), delimiter=",")
ta=np.array(list(reader)).astype("int")
reader=csv.reader(open(sys.argv[2], "rU"), delimiter=",")
tb=np.array(list(reader)).astype("int")
reader=csv.reader(open(sys.argv[3], "rU"), delimiter=",")
tx=np.array(list(reader)).astype("int")
k=np.kron(tx,tx)
taf=ta.flatten()
kp=np.delete(k,np.nonzero(1-taf),0)
tbf=tb.flatten()
tbp=tbf[taf==1]
f = open('workfile.txt', 'w')
kk=np.dot(kp.transpose(),kp)

#alpha=0.215
for alpha in np.arange(float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6])):
	ka=np.linalg.inv(kk+alpha*np.identity(kk.shape[1]))
	ka=np.dot(ka,kp.transpose())
	ky=np.dot(kp,ka)
	tau=np.trace(np.identity(ky.shape[1])-ky)
	tof=np.dot(ka,tbp)
	r=np.linalg.norm(tbp-np.dot(kp,tof))
	obj=r*r/tau/tau
	f.write(str(alpha) + "\t" + str(obj) + "\n")
	tof=tof.reshape(tx.shape[1],tx.shape[1])
	np.savetxt("rule_matrix_"+format(alpha,'.4f')+".csv",tof, delimiter=",")

kpinv=np.linalg.pinv(kp)
oMP=np.dot(kpinv,tbp)
of=oMP.reshape(tx.shape[1],tx.shape[1])
np.savetxt("rule_matrix_MP.csv",of, delimiter=",")
