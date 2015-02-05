import yaml
import paho.mqtt.client as mqtt

"""
Report the events to the broker
"""
class Reporter:
    def __init__(self, dockerClient, cfgFile = "agent.yml", loginFile = "login.yml"):
        # We need to specify the protocol as the mosquitto broker provided with debian 7
        # is broken and cannot detect the protocol version
        # cf. https://bugs.eclipse.org/bugs/show_bug.cgi?format=multiple&id=446062
        self.mqtt = mqtt.Client(protocol=mqtt.MQTTv31)

        with open(cfgFile, 'r') as ymlfile:
            self.cfg = yaml.load(ymlfile)
        with open(loginFile, 'r') as ymlfile:
            self.login = yaml.load(ymlfile)

    """Connect to the MQTT broker"""
    def connect(self):
        self.mqtt.connect(self.cfg['server'])

    """Publish a message to the MQTT broker"""
    def report(self, event):
        self.mqtt.reconnect()
        self.mqtt.publish(self.cfg['topic'], event.json(self.login['username'], self.login['password']))
