# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""


from concurrent.futures import ThreadPoolExecutor
import os

def ping(host):
    result = os.system('ping -c 3 ' + host)
    return result

def ping_ip_addresses(ip_list, limit=3):
    reachable = []
    unreachable = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(ping,ip_list)
        for device, output in zip(ip_list, result):
            if output:
                unreachable.append(device)
            else:
                reachable.append(device)
        final_result = (reachable, unreachable)
    return final_result

if __name__ == "__main__":
    list_of_ips = ["1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
    print(ping_ip_addresses(list_of_ips))



