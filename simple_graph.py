import networkx as nx
import matplotlib.pyplot as plt

# G = nx.Graph()# Graph
G = nx.DiGraph()# Directed Graph
G.add_node(1)
G.add_nodes_from([2, 3, "AAA"])
G.add_edge(1, 2)
G.add_edge(3, "AAA")
# print(list(G.nodes))
# print(list(G.edges))

# G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
plt.savefig("./graph_image.png")