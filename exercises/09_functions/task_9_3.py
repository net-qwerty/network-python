# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


# def get_int_vlan_map(config_file):
#     f = open(config_file,'r')
#     iter = 0
#     text=f.read().strip().split('\n')
# #    print(text)
#     config = []
#     conf_trunk={}
#     conf_acces={}
#     print(text)
#     for command in text:
#         command.lstrip()
#         if command.startswith('!'):
#             continue
# #        print(command.startswith('interface'))
# #        print(text[iter + 1].startswith(' switchport'))
#         if command.startswith('interface') and text[iter + 1].startswith(' switchport'):
#             print(text[iter + 1])
#             if " switchport trunk encapsulation dot1q" in text[iter + 1]:
#                 print(command)
#                 inter=command.split()
#                 print(inter)
#             #    conf_trunk.setdefault(inter[-1])
#                 vlanstr=text[iter + 2].split()[-1].split(",")
#                 vlanint=[]
#                 for val in vlanstr:
#                     vlanint.append(int(val))
#                 conf_trunk[inter[-1]]=vlanint
#             elif "switchport mode access" in text[iter + 1]:
#                 inter=command.split()
#             #    conf_acces.setdefault(inter[-1])
#                 print(inter[-1])
#                 vlan=int(text[iter + 2].split()[-1])
#                 conf_acces[inter[-1]]=vlan
#        # print(conf_trunk)
#        # print(conf_acces)
#         iter += 1
#     print(conf_trunk)
#     print(conf_acces)

def get_int_vlan_map(config_filename):
    conf_trunk={}
    conf_acces={}
    with open(config_filename) as text:
        for command in text:
            command=command.rstrip()
            if command.startswith('!'):
                continue
            elif command.startswith('interface'):
                inter=command.split()[-1]
            elif "trunk allowed" in command:
                vlanstr=command.split()[-1].split(",")
                vlanint=[]
                for val in vlanstr:
                    vlanint.append(int(val))
                conf_trunk[inter]=vlanint
            elif "access vlan" in command:
                    #print(inter[-1])
                vlan=int(command.split()[-1])
                conf_acces[inter]=vlan

        return (conf_acces,conf_trunk)


print(get_int_vlan_map("/home/sadm/files/cource/network-python/exercises/09_functions/config_sw1.txt"))
