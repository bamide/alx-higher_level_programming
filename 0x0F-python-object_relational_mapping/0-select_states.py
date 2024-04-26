#!/usr/bin/python3
""" This script list all states from the database "hbtn_0e_0_usa."""


import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MYSQL server
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to select all states and sort them by id
    query = "SELECT * FROM `states`"
    cursor.execute(query)

    # Fetch all rows
    states = cursor.fetchall()

    # Print results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
