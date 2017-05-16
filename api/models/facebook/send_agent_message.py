from chatbase.config.config_handler import ReadConfig
from chatbase.api.exceptions.common import ConfigException


class SendAgentMessage:
    """Facebook Native Send Agent Message Model"""

    payload = None
    schema = {
        "type": "object",
        "properties": {
            "request_body": {
                "type": "object",
                "properties": {
                    "recipient": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string"
                            }
                        }
                    },
                    "message": {
                        "type": "object",
                        "properties": {
                            "text": {
                                "type": "string"
                            }
                        }
                    }
                },
                "optional": True,
                "recommended": True
            },
            "response_body": {
                "type": "object",
                "properties": {
                    "recipient_id": {
                        "type": "string"
                    }
                }
            },
            "chatbase_fields": {
                "type": "object",
                "properties": {
                    "version": {
                        "type": "string",
                        "optional": True
                    }
                }
            }
        }
    }

    def __init__(self):
        config = ReadConfig.get_config("general")
        if config.__len__() < 1:
            msg = "Section general not found"
            raise ConfigException("Error from {} ===>>> {}".format(str(SendMessage).replace("<", "").replace(">", "").replace("'", "").replace("class", "").replace(" ", ""), msg))
        else:
            self.url = config["base_url"]
            self.api_key = config["api_key"]