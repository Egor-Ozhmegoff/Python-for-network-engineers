# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
<<<<<<< HEAD
ospf_route=ospf_route.replace(',',' ')
ospf=list(ospf_route.split())
ospf[1]=ospf[1].strip('[]')
ospf.remove('via')
ospf_keys=['Perfix','AD/Metric','Next-Hop','Last Update','Outbound Interface']
ospf_dict=dict(zip(ospf_keys,ospf))
ospf_dict
=======
>>>>>>> template/master
