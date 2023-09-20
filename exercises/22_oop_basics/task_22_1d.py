# -*- coding: utf-8 -*-

"""
Задание 22.1d

Изменить класс Topology из задания 22.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще
 нет в топологии.
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение
"Соединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Соединение с одним из портов существует


"""
from pprint import pprint

class Topology:
    topology = {}
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        for key, value in topology_dict.items():
            if not type(self).topology.get(value) == key:
                type(self).topology[key] = value
        return type(self).topology
    
    def delete_link(self, val1, val2):
        if type(self).topology.get(val1) == val2:
            del type(self).topology[val1]
        elif type(self).topology.get(val2) == val1:
            del type(self).topology[val2]
        else:
            print("Такого соединения нет")
    
    def delete_node(self,node):
        found=False
        iter=type(self).topology.copy()
        for key,value in iter.items():
            if node in (key+value):
                del type(self).topology[key]
                found = True
        if not found:
            print("Такого устройства нет")

    def add_link(self,addl_src,addl_dst):
        iter=type(self).topology.copy()
        found=False
        for key,value in iter.items():
            if addl_src == key or addl_src == value or addl_dst == key or addl_dst == value:
                print("Соединение с одним из портов существует")
                found=True
        if type(self).topology.get(addl_src) == addl_dst:
            print("Такое соединение существует")
        elif not found:
            type(self).topology[addl_src]=addl_dst
    

if __name__ == "__main__":
    topology_example = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    }


    topology1=Topology(topology_example)
    pprint(topology1.topology)
    topology1.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    pprint(topology1.topology)