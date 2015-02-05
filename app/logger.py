from reporter import Reporter
from event import Event
import time

"""
Manages the containers logs
"""
class Logger:
    def __init__(self, docker_client):
        self.docker = docker_client
        self.reporter = Reporter(self.docker)
        # keep the last read log line for each container
        # workaround because of the problem with log streaming
        self.state = {}

    """Fetches the logs and sends them to the broker"""
    def read_logs(self, log_filter):
      self.reporter.connect()
      while True:
        time.sleep(10)
        for container in self.docker.containers():
          container_id = container["Id"].encode('ascii','ignore')
          if not self.state.has_key(container_id):
              self.state[container_id] = 0
          if not "tsp-mooc-" in container["Image"]:
            for log in self.docker.logs(container=container["Id"], timestamps=True).split('\n')[self.state[container_id]:]:
                print log
                if log_filter in log:
                    self.reporter.report(Event("mooc", log[31:], container["Image"], log[:30]))
                self.state[container_id] = self.state[container_id] + 1
