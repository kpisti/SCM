import numpy as np
import csv
reader=csv.reader(open("GapJunctContact.csv", "rU"), delimiter=",")
ta=list(reader)
ta=np.array(ta).astype("int")
reader=csv.reader(open("alpha_exp_GapJunctContact.txt_ContactSubgraphMatrix.txt_100.csv", "rU"), delimiter=",")
tb=list(reader)
tb=np.array(tb).astype("double")
reader=csv.reader(open("INXExpressionJustContact.csv", "rU"), delimiter=",")
tx=list(reader)
tx=np.array(tx).astype("int")
kp=np.kron(tx,tx)
#taf=ta.flatten()
#kp=np.delete(k,np.nonzero(1-taf),0)
tbp=tb.flatten()
#tbp=tbf[taf==1]
#f = open('workfile', 'w')
kk=np.dot(kp.transpose(),kp)

alpha=0.001

ka=np.linalg.inv(kk+alpha*np.identity(kk.shape[1]))
ka=np.dot(ka,kp.transpose())

tbs=tbp*(1.0-tbp)

tof=np.dot(ka,tbp)
tof=tof.reshape(tx.shape[1],tx.shape[1])
np.savetxt("rule_matrix_"+format(alpha,'.4f')+"rnd_av.csv",tof, delimiter=",")

kaa=abs(ka)
tos=np.dot(kaa,tbs)
tos=tos.reshape(tx.shape[1],tx.shape[1])
np.savetxt("rule_matrix_"+format(alpha,'.4f')+"rnd_var.csv",tos, delimiter=",")

