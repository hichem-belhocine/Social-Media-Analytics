import numpy as np
import snap 
import networkx as nx
import matplotlib.pyplot as plt

email_graph = nx.read_edgelist("email-Eu-core.txt" )

#Clustering Coefficient 
clustering = snap.GetClustCf(email_graph) 
print("Clustering Coefficient", clustering)

#Average Path Length
avr_path_length = snap.GetShortPath(email_graph)
print("Average Path Length", avr_path_length)

#Degree Distribution
degree = np.zeros(email_graph.GetNodes())
for node in email_graph.Nodes():
    degree[node.GetId()] = node.GetInDeg()
plt.hist(degree, bins=10)
