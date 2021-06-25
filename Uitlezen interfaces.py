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
        description = ['description']
        print(f"{name}: {description}")


if __name__ == "__main__":
    data = get_interfaces()
    show_interfaces(data)