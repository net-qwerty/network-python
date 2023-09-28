# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
file = open('ospf.txt', 'r')
template = '''Prefix                {prefix}
AD/Metric             {admet}
Next-Hop              {hop}
Last update           {update}
Outbound Interface    {outint}'''
text=file.read().rstrip().split('\n')
for route in text:
    routelist=route.split()
    print(template.format(prefix=routelist[1], admet=routelist[2].strip('[]'), hop=routelist[4].rstrip(','), update=routelist[5].rstrip(','), outint=routelist[6]))
        
