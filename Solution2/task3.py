import networkx as nx
import matplotlib.pyplot as plt
import operator

# load the graph with networkx
G = nx.read_edgelist('./email-Eu-core.txt')

#Print the node with the highest centrality score using page rank
PageRank_G = nx.pagerank(G)
max_node = max(PageRank_G, key=PageRank_G.get)
max_rank = PageRank_G[max_node]
print('Node: ' + str(max_node) + ', max page rank: ' + str(max_rank))

   

# Print the centrality score for each node using EigenVector Centrality
eigenvector_G = nx.eigenvector_centrality(G)
for Centrality_Scores in eigenvector_G:
	print ("node: " + str(Centrality_Scores) + " eigenvector centrality: "  + str(eigenvector_G[Centrality_Scores]))



