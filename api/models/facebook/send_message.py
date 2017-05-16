from chatbase.config.config_handler import ReadConfig
from chatbase.api.exceptions.common import ConfigException


class SendMessage:
    """Facebook Native Send Message Model"""

    sender_id = None
    recipient_id = None
    timestamp = None
    message_text = None
    intent_str = None
    not_handled = None
    feedback = None
    version = None
    url = None
    api_key = None

    def __init__(self):
        config = ReadConfig.get_config("general")
        if config.__len__() < 1:
            msg = "Section general not found in config"
            raise ConfigException("Error from {} ===>>> {}".format(str(SendMessage).replace("<", "").replace(">", "").replace("'", "").replace("class", "").replace(" ", ""), msg))
        else:
            self.url = config["base_url"]
            self.api_key = config["api_key"]