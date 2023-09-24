import os
import sqlite3
import re

db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'

db_exists = os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

if not db_exists:
    print('Создаю базу данных...')
    with open(schema_filename, 'r') as f:
        schema = f.read()
    conn.executescript(schema)
    print('Done')
else:
    print('База данных существует')

conn.close()