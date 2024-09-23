import pyodbc


def get_mssql_connection():
    try:
        DRIVER = 'ODBC driver 17 for SQL Server'
        HOST = 'innalytics.database.windows.net'
        USER = 'AppUser2'
        PASSWORD = 'Iec@420#1234'
        DB = 'TestCoreDB'
        conn = pyodbc.connect(
            'DRIVER={' + DRIVER + '};SERVER=' + HOST + ';DATABASE=' + DB + ';UID=' + USER + ';PWD=' + PASSWORD)
        return conn
    except Exception as e:
        print("get_mssql_connection " + str(e))


def get_result(query):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.execute(query)
    row = cursor_str.fetchall()
    mssql_conn.close()
    return row


def get_result_col(query):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.execute(query)
    row = cursor_str.fetchall()
    column_names = [column[0] for column in cursor_str.description]
    mssql_conn.close()
    return row, column_names


def put_result(query, data):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.execute(query, data)
    mssql_conn.commit()
    mssql_conn.close()
    return cursor_str.rowcount


def put_result1(query):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.execute(query)
    mssql_conn.commit()
    mssql_conn.close()
    return cursor_str.rowcount


def put_result2(qry, pram):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.executemany(qry, pram)
    mssql_conn.commit()
    mssql_conn.close()
    return cursor_str.rowcount


def call_prop(qry, params):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.execute(qry, params)
    mssql_conn.commit()
    mssql_conn.close()
    return cursor_str.rowcount


def call_prop1(qry, params):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.execute(qry, params)
    row = cursor_str.fetchall()
    column_names = [column[0] for column in cursor_str.description]
    mssql_conn.close()
    return row, column_names


def call_prop_col_without_param(qry):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.execute(qry)
    row = cursor_str.fetchall()
    column_names = [column[0] for column in cursor_str.description]
    mssql_conn.close()
    return row, column_names


def call_prop_return_pk(qry, params):
    mssql_conn = get_mssql_connection()
    cursor = mssql_conn.cursor()
    cursor.execute(qry, params)
    output_id = cursor.fetchone()[0]
    mssql_conn.commit()
    mssql_conn.close()
    return output_id