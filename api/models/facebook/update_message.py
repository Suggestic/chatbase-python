from chatbase.config.config_handler import ReadConfig
from chatbase.api.exceptions.common import ConfigException
import jsonschema as js


class UpdateMessage:
    """Facebook Native Update Message Model"""

    payload = None
    message_id = None
    schema = {
        "intent": {
            "type": "string",
            "optional": True
        },
        "not_handled": {
            "type": "string",
            "optional": True
        },
        "feedback": {
            "type": "string",
            "optional": True
        },
        "version": {
            "type": "string",
            "optional": True
        }
    }

    def __init__(self):
        config = ReadConfig.get_config("general")
        if config.__len__() < 1:
            msg = "Section general not found"
            raise ConfigException("Error from {} ===>>> {}".format(str(UpdateMessage).replace("<", "").replace(">", "").replace("'", "").replace("class", "").replace(" ", ""), msg))
        else:
            self.url = config["base_url"]
            self.api_key = config["api_key"]