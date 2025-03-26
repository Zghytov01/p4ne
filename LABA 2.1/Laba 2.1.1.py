import requests


headers = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}


r = requests.get(
    'https://10.31.70.209/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces',
    auth=("restapi", "j0sg1280-7@"),
    headers=headers,
    verify=False
)


if r.status_code == 200:
    output_list = r.json()['Cisco-IOS-XE-interfaces-oper:interfaces']['interface']

    interface_list = []
    for interface in output_list:
        interface_list.append(
            f"Interface: {interface['name']}\n"
            f"Packets: {interface['v4-protocol-stats']['out-pkts']} "
            f"Bytes: {interface['v4-protocol-stats']['out-octets']}"
        )


    for item in interface_list:
        print(item)
else:
    print(f"Error: {r.status_code} - {r.text}")