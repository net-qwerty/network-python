# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress
from task_12_1 import ping_ip_addresses

def convert_ranges_to_ip_list(ip_list):
    ip_listr=[]
    for ip in ip_list:
        if "-" in ip:
            range=ip.split("-")
            i=0
            if len(range[-1]) >= 4:
                result=int(range[1].split(".")[-1])-int(range[0].split(".")[-1])
                ipn = ipaddress.ip_address(range[0])
                ip_listr.append(str(ipn))
                while i < result:
                    i += 1
                    ipn += 1
                    ip_listr.append(str(ipn))
            elif len(range[-1]) < 4:
                result=int(range[1])-int(range[0].split(".")[-1])
                ipn = ipaddress.ip_address(range[0])
                ip_listr.append(str(ipn))
                while i < result:
                    i += 1
                    ipn += 1
                    ip_listr.append(str(ipn))
        else:
            ip_listr.append(str(ip))
                    
    return ip_listr

if __name__ == "__main__":
    ip = ["192.168.0.5-192.168.0.8", "10.0.0.55-10.0.0.57", "99.99.99.99", "8.8.8.8", "8.8.4.4"]
    print(ping_ip_addresses(convert_ranges_to_ip_list(ip)))