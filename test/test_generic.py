import unittest
from chatbase.api.generic.generic import GenericSendMessages
from chatbase.api.generic.generic import GenericUpdateMessage


class MyTestCase(unittest.TestCase):

    def test_send_messages(self):

        payload = {
            "u_type": "agent",
            "user_id": "1234567890",
            "platform": "test_chatbase",
            "message": "Hola Mundo !!",
            "intent": "greeting",
            "not_handled": False,
            "version": "1.0"
        }
        payload2 = {
            "u_type": "user",
            "user_id": "0987654321",
            "platform": "test_chatbase",
            "message": "Hola Mundo !!",
            "intent": "greeting",
            "not_handled": False,
            "feedback": True,
            "version": "1.0"
        }

        agent = GenericSendMessages(payload)
        res1 = agent.send()
        print(res1)

        user = GenericSendMessages(payload2)
        res2 = user.send()
        print(res2)

        self.assertTrue(res1["status"], 200)
        self.assertTrue(res2["status"], 200)

    def test_update_message(self):

        payload = {
            "intent": "greeting",
            "not_handled": False,
            "feedback": True,
            "version": "1.0"
        }

        update = GenericUpdateMessage(payload, "91204686")
        res = update.send()
        print(res)

        self.assertTrue(res["status"], 200)

if __name__ == '__main__':
    unittest.main()
