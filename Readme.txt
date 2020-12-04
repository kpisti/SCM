#This folder contains the processed input files and the codes to obtain the outputs
#Example usage (with python v2.7):

####################Input data files:
###################
#Neuron names of columns and rows:
NeurNamesContact.csv#B matrix for gap junctions with Cook et al. data:GapJunctContact.csv
GapJunctContact.txt
#B matrix for gap junctions with Varshney et al. data:
CEO_Gap_OnlyContact.csv
#C matrix:ContactSubgraphMatrix.csvContactSubgraphMatrix.txt
#X matrix of labels corresponding to innexin expression:
INXExpressionJustContact.csv
###################
#Solving the SCM in a range of alpha regularization parameter values:
###################
python SCM_alpha.py ContactSubgraphMatrix.csv GapJunctContact.csv INXExpressionJustContact.csv 0.215 0.219 0.005
#This leads to the output files:
#workfile.txt -> Values of r^2/tau^2 for each tested alpha regularization parameter to determine the optimal alpha=0.215
#rule_matrix_MP.csv -> alpha->0 solution with the Moore-Penrose pseudo-inverse#rule_matrix_0.2150.csv -> regularized solution with the optimal alpha=0.215


###################
#Network randomization based on Maximum Entropy:
###################
g++ -O3 alpha_matrix.cpp -o alpha_matrix.out
#The size of the input matrix is 185 and we run the randomization for 100 iterations:
#Note that neuron self-interactions are set to zero and are not randomized! This can be changed easily by uncommenting line 111.
./alpha_matrix.out GapJunctContact.txt ContactSubgraphMatrix.txt 185 100
#This leads to the output files:
#alpha_exp_GapJunctContact.txt_ContactSubgraphMatrix.txt_100.csv -> randomized connection probability of each link between the nodes in GapJunctContact.txt, with the spatial constraints in ContactSubgraphMatrix.txt
#alpha_GapJunctContact.txt_ContactSubgraphMatrix.txt_100.txt -> the alpha parameter of each node
python SCM_alpha_rnd.py ContactSubgraphMatrix.csv alpha_exp_GapJunctContact.txt_ContactSubgraphMatrix.txt_100.csv INXExpressionJustContact.csv 0.215
#This leads to the output files:
#rule_matrix_0.2150rnd_av.csv -> mean value of each rule in the randomized ensemble
#rule_matrix_0.2150rnd_var.csv -> variance of each rule in the randomized ensemble