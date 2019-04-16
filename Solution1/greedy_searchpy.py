#Incomplete code for Ex01 Task 4

import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Queue:
    def __init__(self):
        self.elements = []
    
    def isEmpty(self):
        return len(self.elements) == 0
    
    def enqueue(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def dequeue(self):
        return heapq.heappop(self.elements)[1]
        
def greedySearchTraverse(G, q, v, dest, previous_node, cost):
    	
	if v == dest:
		return
	else:
		for node in G[v]: # Get neighbors of v node
			if node in cost:
				continue
			new_cost = cost[v] + float(G[node][v]['cost'])
			cost[node] = new_cost
			# Enqueue the heuristic of this node into the queue
			
			q.enqueue(node, float(heuristics[node]))
			
			previous_node[node] = v
			
			
		greedySearchTraverse(G, q, q.dequeue(), dest, previous_node, cost) 
	
def greedySearch(G, source, dest, heuristics): 
	
	final_path = []
    
	previous_node = {} 
	previous_node[source] = None
	
	cost = {}
	cost[source] = 0
	
	q = Queue()
	q.enqueue(source, 0)
	greedySearchTraverse(G, q, q.dequeue(), dest, previous_node, cost) 
	
	# Reconstruct path
	final_path.append(dest)
	current = dest
	while (current is not source):
		current = previous_node[current]
		final_path.append(current)
	
	return final_path


def readHeuristics(G):
	heuristics = {}	
	f = open('./users_heuristics.txt')
	
	for i in G.nodes():
		node_heuristic_val = f.readline().split()
		heuristics[node_heuristic_val[0]] = node_heuristic_val[1]
	return heuristics

#Input Graph
def CreateGraph():
	G = nx.Graph()
	f = open('./users_edgelist.txt')
	for i in f:
		graph_edge_list = i.split()
		G.add_edge(graph_edge_list[0], graph_edge_list[1], cost = graph_edge_list[2]) 
	source, dest= 'Kate', 'Vera'
	return G, source, dest

# Plot Graph
def DrawGraph(G, source, dest):
	pos = nx.spring_layout(G)
	val_map = {}
	val_map[source] = 'green'
	val_map[dest] = 'red'
	values = [val_map.get(node, 'blue') for node in G.nodes()]
	nx.draw(G, pos, with_labels = True, node_color = values, edge_color = 'b' ,width = 1, alpha = 0.7) 
	edge_labels = dict([((u, v,), d['cost']) for u, v, d in G.edges(data = True)])
	nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.5, font_size = 11) 
	return pos

# Highlight greedy path
def DrawGreedyPath(final_path):
	prev = -1
	for var in final_path:
		if prev != -1:
			curr = var
			nx.draw_networkx_edges(G, pos, edgelist = [(prev,curr)], width = 2.5, alpha = 0.8, edge_color = 'black')
			prev = curr
		else:
			prev = var

#main function
if __name__ == "__main__":
	G, source,dest = CreateGraph()
	pos = DrawGraph(G, source, dest)
	heuristics = readHeuristics(G)
	path = greedySearch(G, source, dest, heuristics)
	DrawGreedyPath(path)
	plt.show()




