from logger import Logger
from docker import Client
import signal
import sys
import yaml

def signal_term_handler(signal, frame):
    print 'terminating...'
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_term_handler)

with open("agent.yml", 'r') as ymlfile:
  cfg = yaml.load(ymlfile)

client = Client(base_url='unix://var/run/docker.sock')

Logger(client).read_logs(cfg['filter'])
