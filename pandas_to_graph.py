"""
This script is to visualize data flow.

In practical uses, expect change like bellow.
- "df" should be created with pd.read_csv()
- "subset_value_dict" should be created acording to accual table naming rule.
- "bbox_inches" should be set acording to image size which you need.

"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import copy

data_list = [
    ["A_001xxxxxxxxxxxxxxxxxxxx", "B_001xxxxxxxxxxxxxxxxxxxx"],
    ["A_002xxxxxxxxxxxxxxxxxxxx", "B_001xxxxxxxxxxxxxxxxxxxx"],
    ["B_001xxxxxxxxxxxxxxxxxxxx", "C_001xxxxxxxxxxxxxxxxxxxx"],
    ["A_001xxxxxxxxxxxxxxxxxxxx", "B_001xxxxxxxxxxxxxxxxxxxx"],
    ["A_011xxxxxxxxxxxxxxxxxxxx", "B_010xxxxxxxxxxxxxxxxxxxx"],
    ["B_010xxxxxxxxxxxxxxxxxxxx", "C_010xxxxxxxxxxxxxxxxxxxx"],
    ["A_012xxxxxxxxxxxxxxxxxxxx", "C_010xxxxxxxxxxxxxxxxxxxx"],
    # ["A_012", "D_001"],# pattern which occurs error
    ]
column_list = [
    'source', 'target'
    ]

df = pd.DataFrame(data = data_list, columns = column_list) # create pandas dataframe
# print(df.head())


G = nx.from_pandas_edgelist(df,
                            source='source',
                            target='target',
                            create_using=nx.DiGraph()
                            )# convert dataframe to graph



attrs = {}
# dictionary to set nodes attribute"subet" like bellow
# attrs = {"A_001": {"subset": 1},
#         "B_001": {"subset": 2},
#         "A_002": {"subset": 1},
#         "C_001": {"subset": 3},
#         }

subset_value_dict = {
    "A":1,
    "B":2,
    "C":3,
    }
for node_i in G.nodes:
    node_prefix = node_i[0]
    subset_value = subset_value_dict[node_prefix]
    attrs[node_i] = {"subset": subset_value}

nx.set_node_attributes(G, attrs)

# TODO: add process which delete nodes that is not connected to specific node.
nodes_to_use = nx.node_connected_component(G, "C_001xxxxxxxxxxxxxxxxxxxx") # Before use this method, It have to convert NON directed graph
print(nodes_to_use)
# tmp_g = copy(G)
# for node_i in G.nodes:
#     if node_i not in nodes_to_use:
#         tmp_g.remove_node(node_i)
# G = tmp_g
pos = nx.multipartite_layout(G)# set layout of nodes grouped by "subset"
fig = plt.figure(figsize=(16.5,11.69))
nx.draw_networkx(G,
                pos,
                with_labels=True,
                font_weight='bold',
                arrows = True,
                arrowsize = 10,
                edge_color = "blue",
                )


plt.savefig("./graph_image.png",
            bbox_inches='tight'
            )