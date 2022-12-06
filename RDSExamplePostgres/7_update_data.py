import psycopg2
import os

def update_info(database,user, password, host, port):
    """ delete part by part id """
    id = "3"
    name = "Johnny Rocket"
    query = """ UPDATE employee 
                SET name = %s
                WHERE id = %s
            """
    
    conn = None
    rows_deleted = 0
    try:
        # read database configuration
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(query, (name, id))
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

    return rows_deleted


print(update_info(
    database="mydb",
    user="postgres",
    password=os.environ["pass.env"],
    host=os.environ["host.env"],
    port='5432'
))