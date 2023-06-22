import json
import networkx as nx
import matplotlib.pyplot as plt

with open("artist_link_dict.json", "r") as f:
    artist_link_dict = json.load(f)

# Print the first few keys of the data dictionary
#print(list(artist_link_dict.values())[:7])

del artist_link_dict['']
#del artist_link_dict["N/A"]
del artist_link_dict["various artists"]

print("enter musician 1")
artist1 = input()

print("enter musician 2")
artist2 = input()

# Create the full graph
graph = nx.Graph()
for artist, collaborations in artist_link_dict.items():
    for collaborator, songs in collaborations.items():
        if collaborator != "" and songs != "" and collaborator !="N/A" and songs != "N/A":
            graph.add_edge(artist, collaborator, song=songs)


k = 7

# Find the shortest path between the two given artists
shortest_path = []
try:
    shortest_path = nx.shortest_path(graph, source=artist1, target=artist2)
except nx.NetworkXNoPath:
    print(f"No path found between {artist1} and {artist2}")
    exit()

# Print the shortest path, and the corresponding songs
for i, artist in enumerate(shortest_path):
    #print(shortest_path)
    if i < len(shortest_path) - 1:
        next_artist = shortest_path[i+1]
        song = graph[artist][next_artist]['song']
        print(f"{artist} -> {next_artist}: {song}")
    else:
        print(artist)
    if i == k:
        print(f"Reached maximum degree of separation ({k}), terminating search.")
        break

print(len(shortest_path)-1)

'''
# Extract a subgraph of nodes that are within k degrees of separation from a given artist
subgraph_nodes = [artist1]
for i in range(k):
    neighbors = []
    for node in subgraph_nodes:
        neighbors.extend(graph.neighbors(node))
    subgraph_nodes.extend(neighbors)

subgraph = graph.subgraph(subgraph_nodes)

# Visualize the subgraph
pos = nx.spring_layout(subgraph)
nx.draw(subgraph, pos=pos, with_labels=True)
plt.show()

'''

