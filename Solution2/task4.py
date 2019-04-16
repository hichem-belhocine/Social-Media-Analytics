import math


#print the similarity scores for each pair of nodes using adamic adar similarity
def adamic_adar_similarity(G):
	for u in G:
		for v in G:
			if u != v and v > u:
				uNeighbors = list(G[u])
				vNeighbors = list(G[v])
				
				commonNeighbors = ''.join(list(set(uNeighbors) & set(vNeighbors)))
				adamic_adar_similarity = 0
				for commonNeighbor in commonNeighbors :
					adamic_adar_similarity = adamic_adar_similarity + 1/ math.log10(len(G[commonNeighbor]))
				print('Adamic Centrality'"("+str(u)+","+str(v)+"): " + str(adamic_adar_similarity))


# Construct Graph from figure3.txt
def CreateGraph():
	G = dict()
	f = open('./figure3.txt')
	for i in f:
		edgelist = i.split()
		if edgelist[0] in G.keys():
			G[edgelist[0]].append(edgelist[1])
		else:
			G[edgelist[0]] = [edgelist[1]]
		if edgelist[1] in G.keys():
			G[edgelist[1]].append(edgelist[0])
		else:
			G[edgelist[1]] = [edgelist[0]]
	return G



# Calculate the minimal path length between start and end node
def minimal_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        minimal = None
        for node in graph[start]:
            if node not in path:
                newpath = minimal_path(graph, node, end, path)
                if newpath:
                    if not minimal or len(newpath) < len(minimal):
                        minimal = newpath
        return minimal
                
# Calculate closeness centrality for the minimal path  
def Closeness_Centrality(G):
	for node in G:
		sum_n = 0
		for other_nodes in G:
			stp = len(minimal_path(G, node, other_nodes))-1			
			sum_n =  sum_n + stp
		print ('Closeness Centrality for node ' +str(node)+" --> "+str(1/(float(sum_n)/(len(G)-1))))



G = CreateGraph()
adamic_adar_similarity(G)
Closeness_Centrality(G)







