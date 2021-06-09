import configparser


def get_config_data(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigFiles/ConfigFile.cfg")
    return config.get(section, key)
