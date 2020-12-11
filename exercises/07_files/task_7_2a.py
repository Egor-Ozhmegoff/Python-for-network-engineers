# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]
with open('config_sw1.txt','r') as f:
    for line in f:
        if '!' in line:
            pass
        elif ignore[0] in line:
            pass
        elif ignore[1] in line:
            pass
        elif ignore[2] in line:
            pass
        else:
            print(line.rstrip())
