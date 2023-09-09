# -*- coding: utf-8 -*-
"""
Задание 21.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show
с помощью netmiko, а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br
и устройствах из devices.yaml.
"""
from textfsm import clitable
import yaml
from netmiko import ConnectHandler

def send_and_parse_show_command(device_dict,command,templates_path,index="index"):
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    attributes={"Command": command, "Vendor": device_dict["device_type"]}
    cli_table = clitable.CliTable(index, templates_path)
    cli_table.ParseCmd(result, attributes)
    header = cli_table.header
    return [dict(zip(header, row)) for row in cli_table]


if __name__ == "__main__":
    with open("devices.yaml") as f:
            devices = yaml.safe_load(f)

    print(send_and_parse_show_command(devices[0],"sh ip int br","templates"))
