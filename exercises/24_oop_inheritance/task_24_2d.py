# -*- coding: utf-8 -*-

"""
Задание 24.2d

Скопировать класс MyNetmiko из задания 24.2c или задания 24.2b.

Добавить параметр ignore_errors в метод send_config_set.
Если передано истинное значение, не надо выполнять проверку на ошибки и метод должен
работать точно так же как метод send_config_set в netmiko.
Если значение ложное, ошибки должны проверяться.

По умолчанию ошибки должны игнорироваться.


In [2]: from task_24_2d import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [6]: r1.send_config_set('lo')
Out[6]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [7]: r1.send_config_set('lo', ignore_errors=True)
Out[7]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [8]: r1.send_config_set('lo', ignore_errors=False)
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-8-704f2e8d1886> in <module>()
----> 1 r1.send_config_set('lo', ignore_errors=False)

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
    
    def send_command(self, command,*args, **kwargs):
        command_output = super().send_command(command,*args, **kwargs)
        self._check_error_in_command(command, command_output)
        return command_output

    def send_config_set(self,commands,ignore_errors=True):
        if type(commands) == str:
            commands=[commands]
        commands_output=""
        if ignore_errors:
            commands_output = super().send_config_set(commands)
        else:
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
    print(device.send_config_set(['lo','sh ip int br'],ignore_errors=True))
#    device.send_command('sh ip br')