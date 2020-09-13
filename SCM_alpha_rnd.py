import numpy as np
import csv
import sys
reader=csv.reader(open(sys.argv[1], "rU"), delimiter=",")
ta=np.array(list(reader)).astype("int")
reader=csv.reader(open(sys.argv[2], "rU"), delimiter=",")
tb=np.array(list(reader)).astype("double")
reader=csv.reader(open(sys.argv[3], "rU"), delimiter=",")
tx=np.array(list(reader)).astype("int")
k=np.kron(tx,tx)
taf=ta.flatten()
kp=np.delete(k,np.nonzero(1-taf),0)
tbf=tb.flatten()
tbp=tbf[taf==1]
kk=np.dot(kp.transpose(),kp)

alpha=float(sys.argv[4])
ka=np.linalg.inv(kk+alpha*np.identity(kk.shape[1]))
ka=np.dot(ka,kp.transpose())

tbs=tbp*(1.0-tbp)
tof=np.dot(ka,tbp)
tof=tof.reshape(tx.shape[1],tx.shape[1])
np.savetxt("rule_matrix_"+format(alpha,'.4f')+"rnd_av.csv",tof, delimiter=",")

kaa=ka*ka
tos=np.dot(kaa,tbs)
tos=tos.reshape(tx.shape[1],tx.shape[1])
np.savetxt("rule_matrix_"+format(alpha,'.4f')+"rnd_var.csv",tos, delimiter=",")
