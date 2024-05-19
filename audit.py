from db import pg


def log(thread, text):
    con = pg.connect()
    #append text to include [LOG]
    text = "[LOG] " + text
    query = "INSERT INTO auditlog (\"thread\", \"text\") VALUES (%s, %s);"
    params = (thread, text)
    pg.execute_insert(con, query, params)

def error(thread, text):
    con = pg.connect()
    #append text to include [ERROR]
    text = "[ERROR] " + text
    query = "INSERT INTO auditlog (\"thread\", \"text\") VALUES (%s, %s);"
    params = (thread, text)
    pg.execute_insert(con, query, params)


def critical(thread, text):
    con = pg.connect()
    #append text to include [ERROR]
    text = "[CRITICAL] " + text
    query = "INSERT INTO auditlog (\"thread\", \"text\") VALUES (%s, %s);"
    params = (thread, text)
    pg.execute_insert(con, query, params)
