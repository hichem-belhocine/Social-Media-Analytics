import networkx as nx
from collections import defaultdict
  
#2-1 Complete the function
def percolated_cliques(G, k):	
        percGraph = nx.Graph()
        cliques_set = [frozenset(c) for c in nx.find_cliques(G) if len(c) >= k]
        #store all information of cliques in a clique set

        percGraph.add_nodes_from(cliques_set)
        #Generate a graph with nodes containing clique information
    
        #Generate a dictionary with node as 'key' and cliques in which they occur as 'value'
        node_cliqueinfo = defaultdict(list)
        for clique in cliques_set:
            for node in clique:
                node_cliqueinfo[node].append(clique)
   
        # For each clique, see which adjacent cliques percolate
        for clique in cliques_set:
            for neighbour_Clique in return_X(clique, node_cliqueinfo):
                if len(clique.intersection(neighbour_Clique)) >= (k - 1):
                    percGraph.add_edge(clique, neighbour_Clique)
    
        # Connected components of clique graph with perc edges
        # are the desired percolated cliques\n",
        for component in nx.connected_components(percGraph):
            yield(frozenset.union(*component))
            #print component
        #return nx.connected_components(percGraph)
            
def return_X(clique, node_cliqueinfo):
	x = set()
	for y in clique:
		for z in node_cliqueinfo[y]:
			if clique != z:
				x.add(z)
	return x
    

  
#2-2 Find the communities in the email conversation graph
G = nx.read_edgelist("email.txt")
for x in percolated_cliques(G, 12):
	print x











