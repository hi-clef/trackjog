# get_timestamp
# Script to retrieve latest data timestamp from MySQL trackjog server.
import mysql.connector as MSC
import sys


# Check for an argument
if len(sys.argv) < 2:
    print("Password needed to execute script.")
    print("Please try again and provide password as argument.")
    exit(1)
else:
    pwd = sys.argv[1]

# Vefify password by attempting to connect to MySQL server
try:
    cnx = MSC.connect(user='matthew', password=pwd, host='10.0.0.129', database='trackjog_test')
    cursor = cnx.cursor()
except MSC.errors.ProgrammingError:
    print("Incorrect password: failed to connect to database.")
    exit(1)


# Execute command to get file timestamp of most recent upload
cursor.execute("SELECT MAX(timestamp) FROM routes")
data = next(cursor)[0]

# Return result to console
if data:
    print(str(data))
else:
    # Default timestamp - earlier than all activity data
    print("2014-01-01 00:00:00")
