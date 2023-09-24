#!/usr/bin/env python3

import os
import sqlite3
import re
import sys
from tabulate import tabulate


def get_all_from_db(filedb, table):
    conn = sqlite3.connect(filedb)
    cursor = conn.cursor()

    print("В таблице dhcp такие записи:")
    query = 'select * from {}'.format(table)
    cursor.execute(query)
    lines=cursor.fetchall()
    lines_active=[]
    lines_noactive=[]
    for line in lines:
        if line[5] == 1:
            lines_active.append(line)
    for line in lines:
        if line[5] == 0:
            lines_noactive.append(line)
    print("Активные записи:\n\n" + tabulate(lines_active) + "\n")
    if lines_noactive:
        print("Неактивные записи:\n\n" + tabulate(lines_noactive))
    conn.close()

def get_key_value_db(filedb, table, key, value):
    conn = sqlite3.connect(filedb)
    cursor = conn.cursor()

    print("Информация об устройствах с такими параметрами:", key, value)
    query = 'select * from {} where {} = ?'.format(table,key)

    cursor.execute(query,(value, ))
    print(tabulate(cursor.fetchall()))

    conn.close()

if __name__ == '__main__':

    db_filename = 'dhcp_snooping.db'
    checkval=["mac", "ip", "vlan", "interface", "switch"]
    

    if len(sys.argv) > 3:
        print("Пожалуйста, введите два или ноль аргументов")
    elif len(sys.argv) == 1:
        get_all_from_db(db_filename,"dhcp")
    elif len(sys.argv) == 3:
        key, value = sys.argv[1:]
        if value in checkval:
            get_key_value_db(db_filename,"dhcp", key, value)
        else:
            print("Данный параметр не поддерживается.\nДопустимые значения параметров: mac, ip, vlan, interface, switch")