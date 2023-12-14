import psycopg2
from psycopg2 import sql


connection = psycopg2.connect(
   dbname = "ruteo",
   user = "chelo",
   password = "chelo",
   host = "localhost",
   port = "5432"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Replace 'your_new_database' with the name you want for your new database
new_database_name = 'ruteo'

# Create a new PostgreSQL database
create_db_query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_database_name))
cursor.execute(create_db_query)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print(f"Database '{new_database_name}' created successfully.")