#!venv/bin/python3

from hcloud import Client
from hcloud.images import Image
from hcloud.server_types import ServerType

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

client = Client(token=api_key)

servers = client.servers.get_all()

for server in servers:
    print(f"{server.name} {server.status}")
