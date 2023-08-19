# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""

from tabulate import tabulate
from task_12_1 import ping_ip_addresses
from task_12_2 import convert_ranges_to_ip_list

def print_ip_table(ip_reachable, ip_unreachable):
    columns = ['Reachable', 'Unreachable']
    table={'Reachable': ip_reachable, 'Unreachable' : ip_unreachable}

    print(tabulate(table, headers="keys"))

ip = ["10.0.0.55-10.0.0.57", "99.99.99.99", "8.8.8.8", "8.8.4.4"]
ready_ip=ping_ip_addresses(convert_ranges_to_ip_list(ip))
print_ip_table(ready_ip[0],ready_ip[1])

