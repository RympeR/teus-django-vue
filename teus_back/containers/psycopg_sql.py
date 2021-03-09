import psycopg2


def execute_query(user, password, query):
<<<<<<< HEAD
    conn = psycopg2.connect(
    #conn = psycopg2.connect(
    #    host="localhost",
    #    database="teos",
    #    user='postgres',
    #    password='1111',
    #    port='5432'
    #)
        host="localhost",
        database="teus",
        user='teus_dev',
        password='teus_dev',
        port='5432'
    )
=======
>>>>>>> 6a516555b4dd1141ae4d640ba90ef150f51f606a
    # conn = psycopg2.connect(
    #     host="localhost",
    #     database="teus",
    #     user='teus_dev',
    #     password='teus_dev',
    #     port='5432'
    # )
    conn = psycopg2.connect(
        host="localhost",
        database="teus",
        user='postgres',
        password='1111',
        port='5432'
    )


    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()


def execute_select_query(user, password, query, f_all=True):
<<<<<<< HEAD
    #conn = psycopg2.connect(
    #    host="localhost",
    #    database="teos",
    #    user='postgres',
    #    password='1111',
    #    port='5432'
    #)
    # conn = psycopg2.connect(
    #     host="localhost",
    #     database="teus",
    #     user='postgres',
    #     password='1111',
    #     port='5432'
    # )
=======
>>>>>>> 6a516555b4dd1141ae4d640ba90ef150f51f606a
    conn = psycopg2.connect(
        host="localhost",
        database="teus",
        user='postgres',
        password='1111',
        port='5432'
    )
    # conn = psycopg2.connect(
    #     host="localhost",
    #     database="teus",
    #     user='teus_dev',
    #     password='teus_dev',
    #     port='5432'
    # )
    cursor = conn.cursor()
    cursor.execute(query)
    if f_all:
        data = cursor.fetchall()
    else:
        data = cursor.fetchone()
    conn.close()
    return data
