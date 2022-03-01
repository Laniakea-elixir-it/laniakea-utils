import configparser
import os

class ConfigurationFileNotFound(Exception):
    """Raised when the laniakea-utils config file does not exists"""

    def __init__(self, message="laniakea-utils configuration file not found."):
        self.message = message
        super().__init__(self.message)


class ReadConfigurationFile:
    def __init__(self):

        # Serch configuration file
        config_file_path_list = ['/etc/laniakea/laniakea-utils.ini']
        if os.getenv("VIRTUAL_ENV") is not None:
            config_file_path_list.append(os.environ['VIRTUAL_ENV']+'/etc/laniakea/laniakea-utils.ini')

        config_file=None
        for i in config_file_path_list:
            if os.path.exists(i):
                config_file = i
                break

        if config_file is None:
            raise ConfigurationFileNotFound

        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    # Section commons
    def get_log_file(self):
        return self.config['commons']['log_to']

    # Section api
    def get_trusted_OP_list(self):
        return self.config['api']['trusted_OP_list']

    def get_trusted_sub(self):
        return self.config['api']['trusted_sub']

prova = ReadConfigurationFile()

print(prova.get_log_file())
print(prova.get_trusted_OP_list())
print(prova.get_trusted_sub())
