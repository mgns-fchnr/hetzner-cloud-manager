#!venv/bin/python3

from hcloud import Client
from hcloud.images import Image
from hcloud.server_types import ServerType

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

client = Client(token=api_key)

def status():

    servers = client.servers.get_all()

    for server in servers:
        print(f"Server: {server.name} - Status: {server.status}")
        print(f"+++++++++++++++++++++++++++++++++++++++++++++++")


print(f"What do you want to do?")
print(f"1 - See status of all servers")
print(f"2 - Create new server (not available now)")
print(f"3 - Exit")

start = input("> ")

if start == "1":
    status()
elif start == "2":
    print("Feature not available now")
elif start == "3":
    exit
else:
    print("Invalid operation")


