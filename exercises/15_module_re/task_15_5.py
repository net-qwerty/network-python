# -*- coding: utf-8 -*-
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать
на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов,
а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""
import re

def generate_description_from_cdp(config):
    result={}
    template="description Connected to {dev} port {int}"
    regax=( r"(?P<device>\w+)  +(?P<intl>\S+ \d+.\d+)" 
            r"  +\d+  +[\w ]+  +\d+ +(?P<intr>\S+ \d+.\d+)" )
    with open(config) as file:
        match=re.finditer(regax,file.read())
#        print(match.groups())
        # for m in match:
        #     print(m['intr'])
#             result[m['intl']] = template.format(dev=m['device'],int=m['intr'])
        result={m['intl']: template.format(dev=m['device'],int=m['intr']) for m in match}
    return result



print(generate_description_from_cdp("/home/sadm/files/cource/network-python/exercises/15_module_re/sh_cdp_n_sw1.txt"))