# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess

def ping_ip_addresses(ip_list):
    '''
    Функция пингует ip адресс и возращает два списка доступными и недоступными ip
    '''
    alive_ip=[]
    unreachable_ip=[]
    for ip_address in ip_list:
        reply = subprocess.run(['ping', '-c', '1', '-n', ip_address],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL,)
        if reply.returncode == 0:
            alive_ip.append(ip_address)
        else:
            unreachable_ip.append(ip_address)
    return alive_ip, unreachable_ip

if __name__ == "__main__":
    list=["8.8.8.8", "3.432.4", "8.8.4.4", "172.16.0.1"]
    print(ping_ip_addresses(list))