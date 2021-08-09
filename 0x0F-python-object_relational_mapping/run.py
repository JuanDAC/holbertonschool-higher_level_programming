#!/usr/bin/python3
"""
Run all states
"""

def run(argv, sql, handler_cursor, handler_error):
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        handler_cursor(cursor)
    except Exception as e:
        handler_error(e)
    db.close()

