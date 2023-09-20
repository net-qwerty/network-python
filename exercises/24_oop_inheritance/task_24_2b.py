# -*- coding: utf-8 -*-

"""
Задание 24.2b

Скопировать класс MyNetmiko из задания 24.2a.

Дополнить функционал метода send_config_set netmiko и добавить в него проверку
на ошибки с помощью метода _check_error_in_command.

Метод send_config_set должен отправлять команды по одной и проверять каждую на ошибки.
Если при выполнении команд не обнаружены ошибки, метод send_config_set возвращает
вывод команд.

In [2]: from task_24_2b import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_config_set('lo')
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-2-8e491f78b235> in <module>()
----> 1 r1.send_config_set('lo')

...
ErrorInCommand: При выполнении команды "lo" на устройстве 192.168.100.1 возникла ошибка "Incomplete command."

"""

from netmiko.cisco.cisco_ios import CiscoIosSSH
import re


class ErrorInCommand(Exception):
    """
    Исключение генерируется, если при выполнении команды на оборудовании,
    возникла ошибка.
    """

class MyNetmiko(CiscoIosSSH):
    def __init__(self, **device):
        super().__init__(**device)
        self.enable()
    
    def _check_error_in_command(self, command, command_output):
        regax = "% (?P<error>.+)"
        message = ('При выполнении команды "{cmd}" на устройстве "{device}" возникла ошибка {error}')

        find_error=re.search(regax,command_output)
        if find_error:
            raise ErrorInCommand(message.format(cmd=command, device=self.host, error=find_error.group("error")))
    
    def send_command(self, command):
        command_output = super().send_command(command)
        self._check_error_in_command(command, command_output)
        return command_output

    def send_config_set(self,commands):
        if type(commands) == str:
            commands=[commands]
        commands_output=""
        for com in commands:
            output = super().send_config_set(com)
            commands_output += output
            self._check_error_in_command(com,output)
        return commands_output

if __name__ == "__main__":
    
    device_params = {
        "device_type": "cisco_ios",
        "ip": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    
    device=MyNetmiko(**device_params)
    device.send_config_set('lo')
#    device.send_command('sh ip br')
