# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ipstate = False

while not ipstate:
    ip=input("Введите ip адрессв формате 10.0.1.1:")
    checkip=ip.split('.')
    checkstr=''.join(checkip)
    ipstate = True
    if len(checkip) == 4 and checkstr.isdigit():
       for octet in checkip:
          if octet.isdigit() and int(octet) >= 0 and int(octet) <= 255:
             ipstate = True
             continue
          else:
             ipstate = False
             break
    else:
       ipstate = False

    if ipstate:   
       if int(checkip[0]) <= 223 and int(checkip[0]) > 0:
          print("unicast")
       elif int(checkip[0]) > 223 and int(checkip[0]) <= 239:
          print("multicast")
       elif ip == "255.255.255.255":
          print("local broadcast")
       elif ip == "0.0.0.0":
          print("unassigned")
       else:
          print("unused")
    else:
       print("Неправильный IP-адрес")