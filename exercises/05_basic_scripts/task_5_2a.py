# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ipmask=input("Введите ip адресс сети в формате 10.1.1.0/24: ")
ip=ipmask.split('/')[0].split('.')

mask=ipmask.split('/')[-1]
maskb="1"*int(mask)+"0"*(32-int(mask))
masklist=[maskb[0:8],maskb[8:16],maskb[16:24],maskb[24:32]]

ip = "{:08b}{:08b}{:08b}{:08b}".format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3]))
ip=ip[0:int(mask)]
ip=ip + "0" * (32-int(mask))
iplist = [ ip[0:8],ip[8:16],ip[16:24],ip[24:32]]


print("Network:\n{:<8}  {:<8}  {:<8}  {:<8}".format(int(iplist[0],2),int(iplist[1],2),int(iplist[2],2),int(iplist[3],2)))
print("{}  {}  {}  {}\n".format(iplist[0],iplist[1],iplist[2],iplist[3]))


print("Mask:\n/"+mask+"\n{:<8}  {:<8}  {:<8}  {:<8}".format(int(masklist[0],2),int(masklist[1],2),int(masklist[2],2),int(masklist[3],2)))
print("{}  {}  {}  {}".format(masklist[0],masklist[1],masklist[2],masklist[3]))