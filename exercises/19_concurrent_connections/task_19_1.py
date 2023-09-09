# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""
import subprocess
from concurrent.futures import ThreadPoolExecutor


def ping_ip(ip):
    '''
    Функция пингует ip адресс и возращает два списка доступными и недоступными ip
    '''
    reply = subprocess.run(['ping', '-c', '1', '-n', ip],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL,)
    ip_state = reply.returncode == 0
    return ip_state

def ping_ip_addresses(ip_list, limit=3):
    '''
    Функция пингует ip адресс и возращает два списка доступными и недоступными ip
    '''
    alive_ip=[]
    unreachable_ip=[]
    with ThreadPoolExecutor(max_workers=limit) as executor:
        results = executor.map(ping_ip, ip_list)
    for ip, res in zip(ip_list,results):
        print(ip,res)
        if res:
            alive_ip.append(ip)
        else:
            unreachable_ip.append(ip)
    return alive_ip, unreachable_ip


if __name__ == "__main__":
    list=["8.8.8.8", "3.432.4", "8.8.4.4", "172.16.0.1"]
    print(ping_ip_addresses(list,4))