import networkx as nx
import matplotlib.pyplot as plt

# load the graph using networkx
G = nx.read_edgelist("./CollegeMsg.txt", nodetype=int, data=(('time',int),), create_using=nx.DiGraph())

# print network information
print (nx.info(G))

nx.draw(G)
plt.show()
