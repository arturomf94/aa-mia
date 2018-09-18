import networkx as nx

# Return set of nodes with in-degree 0
def in_degree_0(G):
	S = []
	nodes = [node for (node, val) in G.nodes().items()]
	for n in nodes:
		if G.in_degree(n) == 0:
			S.append(n)
	return S

def topological_sort(G):
	L = []
	S = in_degree_0(G)
	while S != []:
		node = S[0]
		L.append(node)
		G.remove_node(node)
		S = in_degree_0(G)
	if G.number_of_edges() > 0:
		return 'G contiene ciclos!'
	return 'Orden: ' + ' '.join(str(e) for e in L)