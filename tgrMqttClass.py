#!/bin/python3
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time
import sys

class TGRMqtt:
    def __init__(self, ipStr, port, username, password):
        self.client = mqtt.Client()
        self.username = username
        self.password = password
        self.ip = ipStr
        self.port = port
        self.client.username_pw_set(username, password)
        self.client.connect(ipStr, port, 60)

    def publish(self, topic, payload):
        self.client.publish(topic, payload=payload, qos=0, retain=False)
    def subscribe(self, callback, topic):
        subscribe.callback(callback, topic, hostname=self.ip, port=self.port, auth ={'username': self.username, 'password': self.password} )

def on_message_print(client, userdata, message):
        print("%s %s" % (message.topic, message.payload))

if __name__ == "__main__":
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    if "--pub" in opts:
        tgrMqtt = TGRMqtt("192.168.0.15", 1883, "tgr_user", "tgr_pass")
        tgrMqtt.publish("led/control",args[0])
    elif "--sub" in opts:
        print(" ".join(arg.upper() for arg in args))
        tgrMqtt = TGRMqtt("192.168.0.15", 1883, "tgr_user", "tgr_pass")
        tgrMqtt.subscribe(on_message_print, "led/status")
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} (--pub | --sub ) <arguments>...")

