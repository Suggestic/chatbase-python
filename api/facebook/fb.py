from chatbase.api.models.facebook.send_message import SendMessage
from chatbase.api.models.facebook.send_agent_message import SendAgentMessage
from chatbase.api.models.facebook.update_message import UpdateMessage
from uuid import uuid4
import jsonschema as js
import requests as req
import time

class FbSendMessage(SendMessage):
    def __init__(self, intent_str, sender, recipient, message_text, not_handled=False, feedback=False, version="1.0"):
        SendMessage.__init__(self)

        self.intent_str = intent_str
        self.sender = sender
        self.recipient = recipient
        self.message_text = message_text
        self.not_handled = not_handled
        self.feedback = feedback
        self.version = version

        self.url = self.url + "/api/facebook/message_received?api_key={}&intent={}&not_handled={}&feedback={}&version={}".format(self.api_key, self.intent_str, self.not_handled, self.feedback, self.version)

        self.payload = {
            "sender": {"id": self.sender},
            "recipient": {"id": self.recipient},
            "timestamp": int(time.time()),
            "message": {
                "mid": "mid.{}".format(uuid4().__str__()),
                "text": self.message_text
            }
        }

    def send(self):

        try:
            r = req.post(self.url, json=self.payload)
            return r.json()

        except Exception as err:
            return {
                "status": 503,
                "reason": err.__str__()
            }


class FbSendAgentMessage(SendAgentMessage):
    def __init__(self, payload):
        SendAgentMessage.__init__(self)

        self.payload = payload

        try:
            js.validate(self.payload, self.schema)

        except js.exceptions.ValidationError:
            msg = "Misconstructed JSON payload"
            raise js.exceptions.ValidationError("Error from {} ===>>> {}".format(str(FbSendAgentMessage), msg))

        self.url = self.url + "/api/facebook/send_message?api_key={}".format(self.api_key)

    def send(self):

        try:
            r = req.post(self.url, json=self.payload)
            return r.json()

        except Exception as err:
            return {
                "status": 503,
                "reason": err.__str__()
            }


class FbUpdateMessage(UpdateMessage):
    def __init__(self, payload, message_id):
        UpdateMessage.__init__(self)

        self.message_id = message_id
        self.payload = payload

        try:
            js.validate(self.payload, self.schema)

        except js.exceptions.ValidationError:
            msg = "Misconstructed JSON payload"
            raise js.exceptions.ValidationError("Error from {} ===>>> {}".format(str(FbSendAgentMessage), msg))

        self.url = self.url + "/api/message/update?api_key={}&message_id={}".format(self.api_key, self.message_id)

    def send(self):

        try:
            r = req.put(self.url, json=self.payload)
            return r.json()

        except Exception as err:
            return {
                "status": 503,
                "reason": err.__str__()
            }