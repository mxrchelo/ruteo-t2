import psycopg2

def fetch_data(conn, table_name, columns):
    """
    Fetch selected columns from a specific table.
    """
    cur = conn.cursor()
    query = f"SELECT {', '.join(columns)} FROM {table_name}"
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    return rows

conn = psycopg2.connect(
   dbname = "routing",
   user = "chelo",
   password = "chelo",
   host = "localhost",
)
# Define the columns you want to retrieve from the "fibra" table
selected_columns = ["probability", "source", "target"]

# Fetch data from the "fibra" table
rows = fetch_data(conn, "fibra", selected_columns)

# Close the connection
conn.close()


for row in rows:
    print(row)