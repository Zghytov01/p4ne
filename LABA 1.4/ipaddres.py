import ipaddress
from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self ):
        ip_addr = random.randint(0x0B000000 , 0xDF000000)
        prefix = random.randint (8,24)
        ipaddress.IPv4Network.__init__(self,(ip_addr,prefix) , strict=False)


# Генерация 50 случайных сетей
networks = [IPv4RandomNetwork() for _ in range(50)]

# Сортировка сетей по возрастанию префикса

#networks.sort(key=lambda net: net.prefixlen)

# Вывод 50 IP-адресов с префиксом
#for network in networks:
    #first_ip = list(network)[0]  # Получаем первый IP-адрес из сети
   # print(f"{first_ip}/{network.prefixlen}")

sorted_networks = sorted(networks, key=lambda net: net.prefixlen)

# Вывод 50 IP-адресов с префиксом
for network in sorted_networks:
    first_ip = list(network)[0]  # Получаем первый IP-адрес из сети
    print(f"{first_ip}/{network.prefixlen}")