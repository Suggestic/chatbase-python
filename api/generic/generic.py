from chatbase.api.models.generic.send_all_messages import SendAllMessages
from chatbase.api.models.generic.update_messages import UpdateMessage
from uuid import uuid4
import jsonschema as js
import requests as req
import time

class GenericSendMessages(SendAllMessages):
    def __init__(self, payload):
        SendAllMessages.__init__(self)

        self.payload = payload
        self.url = self.url

        try:
            js.validate(self.payload, self.schema)
            self.payload["api_key"] = self.api_key
            self.payload["timestamp"] = int(time.time())
            self.payload["type"] = self.payload["u_type"]
            self.payload.pop("u_type")

        except js.exceptions.ValidationError as err:
            msg = "Misconstructed JSON payload: {}".format(err)
            raise js.exceptions.ValidationError("Error from {} ===>>> {}".format(str(GenericSendMessages), msg))

        self.url = self.url + "/api/message"

    def send(self):

        try:
            r = req.post(self.url, json=self.payload)
            return r.json()

        except Exception as err:
            return {
                "status": 503,
                "reason": err.__str__()
            }

class GenericUpdateMessage(UpdateMessage):
    def __init__(self, payload, message_id):
        UpdateMessage.__init__(self)

        self.payload = payload
        self.message_id = message_id
        self.url = self.url

        try:
            js.validate(self.payload, self.schema)

        except js.exceptions.ValidationError as err:
            msg = "Misconstructed JSON payload: {}".format(err)
            raise js.exceptions.ValidationError("Error from {} ===>>> {}".format(str(GenericSendMessages), msg))

        self.url = self.url + "/api/message/update"

    def send(self):

        try:
            params = {
                "api_key": self.api_key,
                "message_id": self.message_id
            }
            r = req.put(self.url, json=self.payload, params=params)
            return r.json()

        except Exception as err:
            return {
                "status": 503,
                "reason": err.__str__()
            }