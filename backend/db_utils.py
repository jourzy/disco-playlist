import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

DB_NAME = "db_disco_playlist"
TEST_DB_NAME = "db_disco_playlist_test"

# Create an exception class called DbConnectionError
class DbConnectionError(Exception):
    pass

# Helper function to establish database connection
def connect_to_db(db_name=TEST_DB_NAME):
    try:
        # Attempt to connect to the DB using provided credentials
        connection = mysql.connector.connect(
            host= os.getenv('HOST'),
            user= os.getenv('USER'),
            password= os.getenv('PASSWORD'),
            database=db_name,
            auth_plugin='mysql_native_password'
        )
        print("Connection to database successful")
        return connection
    
    except Exception as e:
        # Raise custom exception if connection fails
        raise DbConnectionError(f"Failed to connect to database: {str(e)}")  

# Show all tables in database
def show_all_tables(db_name):
    try:
        db = connect_to_db(db_name)
        mycursor = db.cursor()
        mycursor.execute("SHOW TABLES")

        for x in mycursor:
            print(x)

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db:
            db.close()
            print("DB connection is closed")

#   Select all records in the 'playlist' table
def get_playlist(db_name):
    try:
        #   Connect to DB
        db = connect_to_db(db_name)

        #   Add cursor object to execute queries / actions in DB
        my_cursor = db.cursor()
        print("Connected to DB: %s" % db_name)

        #   Query to select all data from playlist and display descending
        query = """SELECT artist, song, votes 
                   FROM tbl_playlist
                   ORDER BY votes DESC;"""

        my_cursor.execute(query)
        result = my_cursor.fetchall() # this is a list with db records where each record is a tuple
    
        #   Close the cursor after query executed
        my_cursor.close()

        # Print and Return the fetched records
        print(result)
        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db:
            db.close()
            print("DB connection is closed")



connect_to_db(DB_NAME)
show_all_tables(DB_NAME)

get_playlist(DB_NAME)
