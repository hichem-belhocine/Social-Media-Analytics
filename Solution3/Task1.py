import networkx as nx
from networkx.algorithms.approximation import clique
import time

G = nx.read_edgelist("email.txt")
k = max(nx.connected_component_subgraphs(G), key=len)

#The total number of cliques in the graph.
cliqueslist =list(nx.find_cliques(k))
print(len(cliqueslist)) # = 3267

#The number of maximal 8-cliques.
maximal_8_cliques =[]

for clq in cliqueslist :
	if len(clq) == 8:
		maximal_8_cliques.append(clq)
print len(maximal_8_cliques) # = 8

#The largest clique(s)
start_time = time.time()
print(clique.max_clique(k))
print("--- % seconds ---" % (time.time() - start_time))

#The laptop blocks always when i execute the largest clique
