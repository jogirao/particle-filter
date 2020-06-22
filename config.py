import os

MAP_FILE="config\map.txt"
ENTITY_FILE="config\entity.txt"

def map_file(path_name=None):
    if not path_name:
        curr_dir=os.path.dirname(__file__)
        return open(os.path.join(curr_dir, MAP_FILE), "r")
    else:
        return open(path_name, "r")
    
def entity_file(path_name=None):
    if not path_name:
        curr_dir=os.path.dirname(__file__)
        return open(os.path.join(curr_dir, ENTITY_FILE), "r")
    else:
        return open(path_name, "r")
