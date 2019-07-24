import socket_tentacles
import json
import requests
import sys
import threading
import json
import queue
import time
import datetime

senders = set()
index = None

class ReceiveHandler(socket_tentacles.ReceiveHandler):
    def handle(self):
        for msg in self.file:
            msg = json.loads(msg)
            if "lat" in msg and "lon" in msg and "timestamp" in msg:
                res = requests.get(index + "/index/interpolate/timestamp?timestamp=%(timestamp)s&lat=%(lat)s&lon=%(lon)s" % msg)
                msg["grib"] = res.json()
            for sender in senders:
                try:
                    sender.put(msg)
                except Exception as e:
                    print(e)
    
class SendHandler(socket_tentacles.SendHandler):
    def handle(self):
        self.queue = queue.Queue()
        try:
            senders.add(self)
            
            while True:
                msg = self.queue.get()
                json.dump(msg, self.file)
                self.file.write("\n")
                self.file.flush()
        finally:
            senders.remove(self)

    def put(self, msg):
        self.queue.put(msg)
            
    def __hash__(self):
        return id(self)
        
def annotator(config):
    index = config["index"]
    socket_tentacles.run(config, {"source": ReceiveHandler, "destination": SendHandler})
