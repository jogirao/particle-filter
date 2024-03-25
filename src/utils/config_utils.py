import os
import csv
import yaml

CONFIG_DIR = "config"
DATA_DIR = "data"


def load_config(config_dir=CONFIG_DIR):
    config_filename = "config.yml"
    yaml_path = os.path.join(config_dir, config_filename)
    with open(yaml_path, 'r') as stream:
        return yaml.safe_load(stream)


def load_text_file(path_name, data_dir=DATA_DIR):
    file_path = os.path.join(data_dir, path_name)
    return [line.rstrip('\n') for line in open(file_path)]


def load_csv_file(path_name, data_dir=DATA_DIR):
    file_path = os.path.join(data_dir, path_name)
    with open(file_path, "r") as stream:
        return [tuple(line) for line in csv.reader(stream)]
