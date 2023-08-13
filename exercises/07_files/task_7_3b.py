# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan=int(input("Enter VLAN number:  "))
file = open("/home/sadm/files/cource/network-python/exercises/07_files/CAM_table.txt",'r')
text=file.read().rstrip().split('\n')
tamplate="{vlan:<8} {mac:<19} {int}"
textsort=[]
for string in text:
    stringn=string.split()
    if ('').join(stringn) != "" and stringn[0].isdigit():
        stringn[0]=int(stringn[0])
        textsort.append(stringn)
textsort.sort()
for stringl in textsort:
    if stringl and type(stringl[0]) == int and stringl[2].isalpha() and stringl[0] == vlan:
        print(tamplate.format(vlan=stringl[0],mac=stringl[1],int=stringl[3]))