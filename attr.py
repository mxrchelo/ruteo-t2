import psycopg2
import networkx as nx

def fetch_data(conn, table_name, columns):
    cur = conn.cursor()
    query = f"SELECT {', '.join(columns)} FROM {table_name}"
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    return rows

def average_two_terminal_reliability(graph):
    total_reliability = 0
    total_pairs = 0

    # Iterate through all pairs of nodes
    for source in graph.nodes():
        for target in graph.nodes():
            if source != target:
                try:
                    # Use all_simple_paths to find all paths between source and target
                    paths = nx.all_simple_paths(graph, source=source, target=target)

                    for path in paths:
                        path_reliability = 1.0
                        for u, v in zip(path[:-1], path[1:]):
                            edge_data = graph[u][v]
                            # Assuming 'probability' is the edge attribute representing failure probability
                            edge_reliability = 1.0 - edge_data.get('probability', 0.0)
                            path_reliability *= edge_reliability

                        total_reliability += path_reliability
                        total_pairs += 1

                except nx.NetworkXNoPath:
                    pass  # No path between source and target

    if total_pairs > 0:
        average_reliability = total_reliability / total_pairs
        return average_reliability
    else:
        return 0.0  # No pairs to calculate average

conn = psycopg2.connect(
   dbname = "routing",
   user = "chelo",
   password = "chelo",
   host = "localhost",
)
selected_columns = ["probability", "source", "target"]
rows = fetch_data(conn, "fibra", selected_columns)
conn.close()

# Create a directed graph
G = nx.DiGraph()

# Iterate through the list of lists and add edges to the graph
for row in rows:
    probability, source, target = row
    G.add_edge(source, target, probability=probability)

#print("Nodes:", G.nodes())
#print("Edges:", G.edges(data=True))
print("ATTR value = ", average_two_terminal_reliability(G))