import psycopg2


def execute_query(user, password, query):
    # conn = psycopg2.connect(
    #     host="localhost",
    #     database="teus",
    #     user=user,
    #     password=password,
    #     port='5432'
    # )
    conn = psycopg2.connect(
        host="localhost",
        database="teos",
        user='postgres',
        password='1111',
        port='5432'
    )


    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()


def execute_select_query(user, password, query, f_all=True):
    conn = psycopg2.connect(
        host="localhost",
        database="teos",
        user='postgres',
        password='1111',
        port='5432'
    )
    # conn = psycopg2.connect(
    #     host="localhost",
    #     database="teus",
    #     user=user,
    #     password=password,
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
