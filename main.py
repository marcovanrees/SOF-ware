import requests
import urllib3

# Disable warning for unverified SSL certificates
urllib3.disable_warnings()

host = "10.10.20.48"
port = 443
username = "developer"
password = "C1sco12345"

url = f"https://{host}:{port}/restconf/data/ietf-interfaces:interfaces"

headers = {
       "Content-Type": "application/yang-data+json",
       "Accept": "application/yang-data+json",
}


def get_interfaces():
    response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    if response.status_code != 200:
        print(f"Error {response.status_code}")
    return response.json()


def show_interfaces(data):
    interface_lijst = data['ietf-interfaces:interfaces']['interface']
    for interface in interface_lijst:
        name = interface['name']
        description = interface['description']
        print(f"{name}: {description}")

def config_interface(num,status):
    configuratie = {
        "ietf-interfaces:interface": {
            "name": f"GigabitEthernet{num}",
            "description": " test1",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": status ,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "11.10.20.48",
                        "netmask": "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6": {
            }
        }
    }
    response = requests.put(url + f"/interface=GigabitEthernet{num}", headers=headers, auth=(username, password), verify=False, json=configuratie)
    print(response.status_code)
    print(response.text)





if __name__ == "__main__":
    data = get_interfaces()         # ophalen van de interface-informatie van de router.
    show_interfaces(data)           # Print de interface met de description.
    config_interface(3,True)        # Wijzig de description en de poort-status (False: admin down, True: admin up)
    data = get_interfaces()
    show_interfaces(data)
