import networkx as nx
import matplotlib.pyplot as plt

# load the graph using networkx
G = nx.read_edgelist("./CollegeMsg.txt", nodetype=int, data=(('time',int),), create_using=nx.DiGraph())

# print network information
print (nx.info(G))

# edges traversed in BFS order starting node 0
print('Depth-first-search traversal (in order):')
dfs = nx.dfs_edges(G, source=1)
print(list(dfs))


