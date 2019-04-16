import networkx as nx
from networkx.algorithms import community

G = nx.read_edgelist("email.txt")
#3-a
component = max(nx.connected_component_subgraphs(G), key=len)

#3-b
communities = community.girvan_newman(component)
ncom = next(communities)
#the number of resulting communities 
num_com = len(ncom)
print("The number of resulting communities is: " +str(num_com)) # = 2

#3-c
first_community=len((ncom)[0])
second_community=len((ncom)[1])
print("The size of the first community is: " +str(first_community)) # = 1130
print("The size of the second community is: " +str(second_community)) # = 3

