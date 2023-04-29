import pymssql

# Define the number of random users to insert
num_users = 10

# Connect to the SQL Server database
conn = pymssql.connect(server='localhost',
                       port=1433,
                       database='devdb',
                       user='sa',
                       password='devDBpassword!@#$')

# Define the SQL statement to create the users table
create_table_sql = """
CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    username NVARCHAR(80) NOT NULL UNIQUE,
    email NVARCHAR(120) NOT NULL UNIQUE
)
"""

# Create the users table
with conn.cursor() as cursor:
    cursor.execute(create_table_sql)
    conn.commit()
    print("Successfully created users table.")

# Close the connection
conn.close()
