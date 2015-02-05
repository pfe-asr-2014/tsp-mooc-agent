import json

"""
Represents an event that can be reported to the MOOC platform
"""
class Event:

    def __init__(self, category, label, action, datetime):
        self.category = category
        self.label = label
        self.action = action
        self.datetime = datetime

    """Format the event in json"""
    def json(self, username, password):
        data = {}
        data['category'] = self.category
        data['action'] = self.action
        data['label'] = self.label
        data['datetime'] = self.datetime
        data['username'] = username
        data['password'] = password
        return json.dumps(data)
