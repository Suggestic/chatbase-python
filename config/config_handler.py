import configparser
import inspect

class ReadConfig:

    @staticmethod
    def get_sections():
        conf = configparser.ConfigParser()
        conf.read("{}/config.conf".format(ReadConfig.get_dir_location(ReadConfig)))
        sections = [section.__str__() for section in conf.sections()]

        return sections

    @staticmethod
    def get_config(section):

        try:
            conf = configparser.ConfigParser()
            conf.read("{}/config.conf".format(ReadConfig.get_dir_location(ReadConfig)))
            config = conf[section]
            return dict(config)

        except:
            return dict()

    @staticmethod
    def get_dir_location(classname):
        return "/".join(inspect.getfile(ReadConfig).split("/")[:-1])