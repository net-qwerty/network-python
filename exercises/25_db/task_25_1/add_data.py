import os
import sqlite3
import re
import yaml
import glob

def add_switch_data(fileyaml,filedb):
    with open(fileyaml) as f:
        dataswitch = yaml.safe_load(f)
    print("Добавляю данные в таблицу switches...")
    connection = sqlite3.connect(filedb)
    query = "INSERT into switches values (?, ?)"
    for row in dataswitch["switches"].items():
        try:
            with connection:
                connection.execute(query, row)
        except sqlite3.IntegrityError as e:
            print(f"При добавлении данных: {row} Возникла ошибка:{e}" )

def add_dhcp_snooping_data(filedhcplist,filedb):
    print("Добавляю данные в таблицу dhcp...")
    connection = sqlite3.connect(filedb)
    regex = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    query = '''insert into dhcp (mac, ip, vlan, interface,switch) values (?, ?, ?, ?, ?)'''
    for file in filedhcplist:
        switch=file.split("_")[0]
        with open(file) as data:
            for line in data:
                match = regex.search(line)
                if match:
                    try:
                        with connection:
                            row=list(match.groups())
                            row.append(switch)
                            connection.execute(query, row)
                    except sqlite3.IntegrityError as e:
                        print(f"При добавлении данных: {match} Возникла ошибка:{e}" )

dhcp_data = glob.glob("*_dhcp_snooping.txt")

add_switch_data("switches.yml","dhcp_snooping.db")
add_dhcp_snooping_data(dhcp_data,"dhcp_snooping.db")
