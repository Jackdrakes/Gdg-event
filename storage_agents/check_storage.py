import pg8000
from pprint import pprint


# Define connection parameters directly
host = "localhost"
port = 5532
database = "ai"  # Your database name
user = "ai"      # Your username
password = "your_password"  # Your password

def db_conn():
    # Create a connection using the defined parameters
    conn = pg8000.Connection(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    return conn

# Use the connection to query the database
conn = db_conn()
try:
    # Replace 'my_table' with the actual table name you want to query
    for row in conn.run("SELECT * FROM agent_sessions;"):  # Change 'my_table' to your actual table name
        pprint(row)
finally:
    conn.close()
