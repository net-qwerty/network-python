# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ipmask=input("Введите ip адресс сети в формате 10.1.1.0/24: ")
ip=ipmask.split('/')[0].split('.')
mask=ipmask.split('/')[-1]
maskb="1"*int(mask)+"0"*(32-int(mask))
masklist=[maskb[0:8],maskb[8:16],maskb[16:24],maskb[24:32]]



print("Network:\n{:<8}  {:<8}  {:<8}  {:<8}".format(ip[0],ip[1],ip[2],ip[3]))
print("{0:08b}  {1:08b}  {2:08b}  {3:08b}\n".format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))


print("Mask:\n/"+mask+"\n{:<8}  {:<8}  {:<8}  {:<8}".format(int(masklist[0],2),int(masklist[1],2),int(masklist[2],2),int(masklist[3],2)))
print("{}  {}  {}  {}".format(masklist[0],masklist[1],masklist[2],masklist[3]))