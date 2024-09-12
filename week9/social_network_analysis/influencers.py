import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes (users)
nodes = ["Aisha", "Ananya", "Kai", "Luca", "Raj", "Yuki"]
G.add_nodes_from(nodes)

# Add edges (following relationships)
edges = [
    ("Ananya", "Raj"),
    ("Ananya", "Yuki"),
    ("Raj", "Yuki"),
    ("Yuki", "Ananya"),
    ("Yuki", "Kai"),
    ("Kai", "Aisha"),
    ("Aisha", "Luca"),
    ("Luca", "Raj"),
    ("Luca", "Ananya")
]
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # positions for all nodes

# Draw nodes and edges
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue', alpha=0.8)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=16, font_family='sans-serif')

# Show the graph
plt.title('Social Network Analysis: Influencer Analysis')
plt.show()