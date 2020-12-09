# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
f = open("ospf.txt","r")

for line in f:
    ospf = " ".join(line.replace(",", " ").replace("[", "").replace("]", "").split())
    ospf_l = list(ospf.split(" "))
    print(f'''
            Prefix                {ospf_l[1]}
            AD/Metric             {ospf_l[2]}
            Next-Hop              {ospf_l[4]}
            Last update           {ospf_l[5]}
            Outbound Interface    {ospf_l[6]}''')
