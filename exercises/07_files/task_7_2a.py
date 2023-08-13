# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
ignore = ["duplex", "alias", "configuration"]
f = open(argv[1],'r')
text=f.read().rstrip().split('\n')

for string in text:
    if string.startswith('!'):
        continue
    comlist=string.split()
    rescheck=True
    for val in comlist:
        if rescheck:
            for ig in ignore:
                if val == ig:
                    rescheck = False 
                    break
        else:
            break
    if not rescheck:
        continue
    else:
        print (string)