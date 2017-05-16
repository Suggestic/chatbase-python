import unittest

from chatbase.config.config_handler import ReadConfig


class TestConfig(unittest.TestCase):
    def test_config(self):

        self.assertNotEqual(0, ReadConfig.get_sections().__len__())
        self.assertNotEqual(0, ReadConfig.get_config("general").__len__())

if __name__ == '__main__':
    unittest.main()
