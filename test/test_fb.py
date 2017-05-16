import unittest
from chatbase.api.facebook.fb import FbSendMessage
from chatbase.api.facebook.fb import FbSendAgentMessage
from chatbase.api.facebook.fb import FbUpdateMessage

class TestFacebook(unittest.TestCase):

    def test_send_message(self):

        fb = FbSendMessage(intent_str="greeting", sender="1234567890", recipient="0987654321", message_text="Hola Mundo !!", not_handled=True, feedback=True, version="1.0")
        res = fb.send()
        self.assertTrue(res["status"], 200)
        print(res)

    def test_send_agent_message(self):

        payload = {
            "request_body": {
                "recipient": {"id": "15208331041"},
                "message": {
                  "text": "hello, world!"
                }
            },
            "response_body": {
                "recipient_id": "15208331041",
                "message_id": "mid.1456970487936:c34767dfe57ee6e339"
            },
            "chatbase_fields": {
                "time_stamp": 1458692752478,
                "version": "1.0"
            }
        }

        fb = FbSendAgentMessage(payload)
        res = fb.send()
        self.assertTrue(res["status"], 200)
        print(res)

    def test_update_message(self):

        payload = {
            " intent " :  " book-flight " ,
            "not_handled": False,
            "feedback": True,
            "version": "1.0"
        }

        message_id = "81619923"

        fb = FbUpdateMessage(payload, message_id)
        res = fb.send()
        self.assertTrue(res["status"], 200)
        print(res)

if __name__ == '__main__':
    unittest.main()
