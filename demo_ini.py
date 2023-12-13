import configparser
from pathlib import Path

DEMO_CONFIG = "demo_config.ini"

def demo_configparser():
    config = configparser.ConfigParser()
    config.read(DEMO_CONFIG)
    #print(config)
    #print(config["DEFAULT"])
    #print(config["DEFAULT"]["environ"])

    for key, value in config["DEFAULT"].items():
        print(key, value)

    #mysql_port = config["mysql"].get("port")    # можно сразу получить число если запрос сделать через getint
    mysql_port = config["mysql"].getint("port")
    print(mysql_port)
    #print([mysql_port])
    mysql_port += 1
    config["mysql"]["port"] = str(mysql_port)

    config["files"]["db"] = str(Path.home())

    with open(DEMO_CONFIG, "w") as file:
        config.write(file, space_around_delimiters=True) # space_around_delimiters=True пробелы между символами




if __name__ == "__main__":
    demo_configparser()