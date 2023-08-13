# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv
ignore = ["duplex", "alias", "configuration"]
f = open(argv[1],'r')
fw= open (argv[2], 'w')
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
    fw.write(string + "\n")
fw.close()