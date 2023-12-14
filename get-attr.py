import networkx as nx

# Assuming G is a NetworkX graph created using pgr_createTopology or any other method
# Define source and target pairs
source_target_pairs = [(1, 5), (2, 4), (3, 6)]

total_reliability = 0
total_pairs = 0

# Iterate over each source-target pair
for source, target in source_target_pairs:
    try:
        # Find the shortest path between source and target nodes
        shortest_path = nx.shortest_path(G, source=source, target=target, weight='length')
        
        # Calculate the reliability of the path (you need to implement this based on your reliability model)
        path_reliability = calculate_path_reliability(G, shortest_path)
        
        # Update total reliability and total pairs
        total_reliability += path_reliability
        total_pairs += 1
    except nx.NetworkXNoPath:
        print(f"No path between {source} and {target}")

# Calculate average reliability
average_reliability = total_reliability / total_pairs

print(f"Average Two-Terminal Reliability: {average_reliability}")
