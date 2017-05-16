# Chatbase Python SDK

This module allows you interact with Google Chatbase API
The submodules are:

- Facebook Native
- Generic

# Facebook Native

### Send Message
For sending simple messages import the class FbSendMessage with the following
parameters:

- intent_str [required]
string
- sender [required]
string
- recipient [required]
string
- message_text [required]
string
- not_handled [optional]
boolean
- feedback [optional]
boolean
- version [optional]
string

```python
from chatbase.api.facebook.fb import FbSendMessage

fb = FbSendMessage(intent_str="greeting", sender="1234567890", recipient="0987654321", message_text="Hello World !!", not_handled=True, feedback=True, version="1.0")

res = fb.send()
```

### Send Agent Message
For sending agent messages import the class FbSendAgentMessage with the following parameters:

- payload [required]
dict

### Example

```python
from chatbase.api.facebook.fb import FbSendAgentMessage
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
```

### Update Message
For updating messages import the class FbUpdateMessage with the following parameters:

- payload [required]
dict
- message_id [required]
string

### Example

```python
from chatbase.api.facebook.fb import FbUpdateMessage
message_id = "9384756"
payload = {
            " intent " :  " book-flight " ,
            "not_handled": False,
            "feedback": True,
            "version": "1.0"
        }
fb = FbUpdateMessage(payload, message_id)
res = fb.send()
```

# Generic

### Send Message
For sending simple messages import the class GenericSendMessages with the following parameters:

- payload [optional]
dict

```python
# For agents

from chatbase.api.generic.generic import GenericSendMessages
payload = {
            "u_type": "agent",
            "user_id": "1234567890",
            "platform": "test_chatbase",
            "message": "Hola Mundo !!",
            "intent": "greeting",
            "not_handled": False,
            "version": "1.0"
        }
agent = GenericSendMessages(payload)
res1 = agent.send()

# For users
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
user = GenericSendMessages(payload2)
res2 = user.send()
```

### Update Message
For updating messages import the class GenericUpdateMessage with the following parameters:

- payload [required]
dict
- message_id [required]
string

### Example

```python
from chatbase.api.generic.generic import GenericUpdateMessage
message_id = "9384756"
payload = {
            "intent": "greeting",
            "not_handled": False,
            "feedback": True,
            "version": "1.0"
        }
update = GenericUpdateMessage(payload, "91204686")
res = update.send()
```

### Todos

 - Develop batch and taps
 - Add documentation to module docs
