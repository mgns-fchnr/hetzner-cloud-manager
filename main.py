#!venv/bin/python3

from hcloud import Client
from hcloud.images import Image
from hcloud.server_types import ServerType

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

client = Client(token=api_key)

def start():
    
    print(f"What do you want to do?")
    print(f"1 - See status of all servers")
    print(f"2 - Create new server (not available now)")
    print(f"3 - Exit")

    choice = input("> ")

    if choice == "1":
        status()
    elif choice == "2":
        print("Feature not available now")
    elif choice == "3":
        exit
    else:
        print("Invalid operation")
        start()

def status():
    
    x = 0
    servers = client.servers.get_all()

    for server in servers:
        if x == 0:
            print(f"+++++++++++++++++++++++++++++++++++++++++++++++")

        print(f"Server: {server.name} - Status: {server.status}")
        print(f"+++++++++++++++++++++++++++++++++++++++++++++++")
        
        x += 1

start()
