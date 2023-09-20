# -*- coding: utf-8 -*-

"""
Задание 23.3a

В этом задании надо сделать так, чтобы экземпляры класса Topology
были итерируемыми объектами.
Основу класса Topology можно взять из любого задания 22.1x или задания 23.3.

После создания экземпляра класса, экземпляр должен работать как итерируемый объект.
На каждой итерации должен возвращаться кортеж, который описывает одно соединение.
Порядок вывода соединений может быть любым.


Пример работы класса:

In [1]: top = Topology(topology_example)

In [2]: for link in top:
   ...:     print(link)
   ...:
(('R1', 'Eth0/0'), ('SW1', 'Eth0/1'))
(('R2', 'Eth0/0'), ('SW1', 'Eth0/2'))
(('R2', 'Eth0/1'), ('SW2', 'Eth0/11'))
(('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
(('R3', 'Eth0/2'), ('R5', 'Eth0/0'))


Проверить работу класса.
"""
from pprint import pprint

class Topology:
    topology = {}
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        normalized_topology = {}
        for key, value in topology_dict.items():
            if not value in normalized_topology:
                normalized_topology[key] = value
        return normalized_topology
    
    def __add__(self, other):
        copy_topology = self.topology.copy()
        copy_topology.update(other.topology)
        return Topology(copy_topology)
    
    def __iter__(self):
        return iter(self.topology.items())
    
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

top = Topology(topology_example)

for link in top:
    print(link)
