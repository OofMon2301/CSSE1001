def read_config(config):
    """Reads the configuration file and returns a dictionary of the settings"""
    config_dict = {}
    with open(config, "r") as config_file:
        for line in config_file:
            if line[0] != "#":
                line = line.strip()
                line = line.split("=")
                config_dict[line[0]] = line[1]
    return config_dict


config = read_config("config.txt")