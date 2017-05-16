from chatbase.config.config_handler import ReadConfig
from chatbase.api.exceptions.common import ConfigException

class SendAllMessages:
    """Generic Send All Messages Model"""

    payload = None
    u_type = None  # User or agent
    timestamp = None
    platform = None
    message = None
    intent = None
    not_handler = None
    feedback = None
    version = None

    schema = {
        "type": "object",
        "properties": {
            "u_type": {
                "type": "string"
            },
            "user_id": {
                "type": "string"
            },
            "platform": {
                "type": "string"
            },
            "message": {
                "type": "string"
            },
            "not_handled": {
                "type": "boolean",
                "optional": True
            },
            "feedback": {
                "type": "boolean",
                "optional": True
            },
            "version": {
                "type": "string",
                "optional": True
            }
        },
        "required": ["u_type", "user_id", "platform", "message"]
    }

    def __init__(self):
        config = ReadConfig.get_config("general")
        if config.__len__() < 1:
            msg = "Section general not found"
            raise ConfigException("Error from {} ===>>> {}".format(str(SendAllMessages).replace("<", "").replace(">", "").replace("'", "").replace("class", "").replace(" ", ""), msg))
        else:
            self.url = config["base_url"]
            self.api_key = config["api_key"]
