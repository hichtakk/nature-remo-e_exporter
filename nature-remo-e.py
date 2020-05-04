#!/usr/bin/env python

from argparse import ArgumentParser
from json import loads
from time import sleep
from urllib.request import Request, urlopen

from prometheus_client import start_http_server, Gauge
from prometheus_client import REGISTRY, PROCESS_COLLECTOR, PLATFORM_COLLECTOR, GC_COLLECTOR

REGISTRY.unregister(PROCESS_COLLECTOR)
REGISTRY.unregister(PLATFORM_COLLECTOR)
REGISTRY.unregister(GC_COLLECTOR)

ENERGY = Gauge("nature_remo_e_kwh", "normal direction cumulative electric energy")
POWER = Gauge("nature_remo_e_kw", "current power")

parser = ArgumentParser()
parser.add_argument("--token", help="access token for Nature Remo Cloud API (https://home.nature.global/)")
parser.add_argument("-p", "--port", help="server listen port")


def send_request(token):
    url = "https://api.nature.global/1/appliances"
    header = {"Authorization": "Bearer {}".format(token)}
    req = Request(url, headers=header)
    data = []
    with urlopen(req) as response:
        data = loads(response.read())
    for device in data:
        properties = device["smart_meter"]["echonetlite_properties"]
        for _property in properties:
            if _property["epc"] == 224:
                ENERGY.set(int(_property["val"]))
            if _property["epc"] == 231:
                POWER.set(int(_property["val"]))

def main():
    args = parser.parse_args()
    start_http_server(18001)
    while True:
        send_request(token=args.token)
        sleep(60)

if __name__ == "__main__":
    main()