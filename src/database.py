import sqlite3


def get_connection():

    conn = sqlite3.connect(
        "database/lol.db"
    )

    return conn

def save_dataframe(
    df,
    table_name
):

    conn = get_connection()

    df.to_sql(
        table_name,
        conn,
        if_exists="append",
        index=False
    )

    conn.close()