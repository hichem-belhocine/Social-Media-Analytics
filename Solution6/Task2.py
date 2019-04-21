import networkx as nx
import matplotlib.pyplot as plt

vertices = 8

#Small World graph
degree = 4
beta = 0.5

#Random graph
probability = 0.4

#Small World graph
small_world = nx.watts_strogatz_graph(vertices, degree, beta)

#Random graph
random_graph = nx.gnp_random_graph(vertices, probability)

#Visualization
plt.axis('off')
pos=nx.circular_layout(random_graph)
nx.draw(random_graph, pos)
plt.show()
print("Random graph")
nx.draw(small_world, pos)
plt.show()
print("Small World")
