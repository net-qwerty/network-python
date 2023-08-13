# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

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