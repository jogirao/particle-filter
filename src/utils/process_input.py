from src.utils.config_utils import load_text_file, load_csv_file
from src.structures import Map, Agent
import ast


def load_map(map_config):
    map_data = load_text_file(map_config['map_path'])
    map_borders = ast.literal_eval(map_data)
    if len(map_borders) == 0 or len(map_borders[0]) == 0:
        raise ValueError(f"{map_config['map_path']} does not contain the desired structure.")
    return Map(map_borders[0], map_borders[1:])


def load_entity(entity_config):
    entity_pose_data = load_text_file(entity_config['entity_pose_path'])
    entity_move_data = load_csv_file(entity_config['entity_move_path'])
    pose, movements = process_entity_data(entity_pose_data, entity_move_data)
    entity = Agent(*pose)
    return entity, movements


def process_entity_data(pose_data, move_data):
    pose = ast.literal_eval(pose_data)
    movements = compute_movements(pose, move_data)
    return pose, movements


def compute_movements(pose, positions):
    # I expect movements to be a list of tuples.
    return [None]
