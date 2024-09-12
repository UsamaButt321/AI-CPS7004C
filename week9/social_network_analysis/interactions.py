import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define nodes (users) and edges (interactions)
nodes = ["User A", "User B", "User C", "User D", "User E", "User F"]
edges = [
    ("User A", "User B"),
    ("User A", "User C"),
    ("User B", "User D"),
    ("User C", "User E"),
    ("User E", "User A"),
    ("User E", "User B"),
    ("User D", "User F"),
    ("User F", "User C")
]
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, seed=42)  # positions for all nodes

# Draw nodes, edges, and labels
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightblue', alpha=0.8)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=16, font_family='sans-serif')

# Title and show plot
plt.title('Twitter User Interaction Network')
plt.show()

# Calculate centrality measures
degree = nx.degree_centrality(G)
print("Degree Centrality:")
for node, cent in degree.items():
    print(f"{node}: {cent:.2f}")

# Calculate betweenness centrality
betweenness = nx.betweenness_centrality(G)
print("\nBetweenness Centrality:")
for node, cent in betweenness.items():
    print(f"{node}: {cent:.2f}")

# Calculate closeness centrality
closeness = nx.closeness_centrality(G)
print("\nCloseness Centrality:")
for node, cent in closeness.items():
    print(f"{node}: {cent:.2f}")

# Calculate eigenvector centrality
eigenvector = nx.eigenvector_centrality(G)
print("\nEigenvector Centrality:")
for node, cent in eigenvector.items():
    print(f"{node}: {cent:.2f}")