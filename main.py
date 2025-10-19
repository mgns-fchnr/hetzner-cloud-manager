#!venv/bin/python3

from hcloud import Client
from hcloud.images import Image
from hcloud.server_types import ServerType

client = Client(token="")

servers = client.servers.get_all()

for server in servers:
    print(f"{server.name} {server.status}")
