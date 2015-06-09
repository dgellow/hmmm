#!/usr/bin/env python2

from mpd import MPDClient
import config

client = MPDClient()

def setup():
    client.connect(config.HOST, config.PORT)

def cleanup():
    client.close()
    client.disconnect()

def reload_config():
    cleanup()
    setup()

def main():
    client.send_idle()
    events = client.fetch_idle()

    for event in events:
        print '[hmmm::event]', event
