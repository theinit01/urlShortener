import sqlite3

def remove_entries():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Execute SQL command to delete all rows from the urls table
    cursor.execute('DELETE FROM urls')

    # Commit the transaction and close the connection
    connection.commit()
    connection.close()
    print("Database is cleaned!!: ))")

if __name__ == '__main__':
    remove_entries()
