# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a
на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них.

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким
образом, чтобы в значении словаря она возвращала список кортежей
для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет
несколько кортежей. Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность
IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re

def get_ip_from_cfg(config):
    '''
    Функция обрабатывает конфигурацию и возвращает IP-адреса и маски,
    которые настроены на интерфейсах, в виде списка кортежей:
    * первый элемент кортежа - IP-адрес
    * второй элемент кортежа - маска
    '''
    regex=( r"^interface (?P<intr>\S+)\n"
            r"|ip address (?P<ip>\S+) (?P<mask>\S+)")
    result={}
    with open(config) as file:
        for line in file:
            match = re.search(regex,line)
            if match:
                if match.lastgroup == "intr":
                    interface=match.group("intr")
                elif match.lastgroup == "mask":
                    result.setdefault(interface,[])
                    result[interface].append((match.group("ip"), match.group("mask")))
    return result

print(get_ip_from_cfg("/home/sadm/files/cource/network-python/exercises/15_module_re/config_r2.txt"))